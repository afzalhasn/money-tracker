import { apiRequest } from "./apiClient";

const ACCESS_TOKEN_KEY = "money-tracker.access-token";
const REFRESH_TOKEN_KEY = "money-tracker.refresh-token";

export type LoginPayload = {
  username: string;
  password: string;
};

export type AuthTokens = {
  access_token: string;
  refresh_token?: string;
  token_type: string;
};

export async function login(payload: LoginPayload): Promise<AuthTokens> {
  const response = await apiRequest("/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const tokens: AuthTokens = await response;
  persistTokens(tokens);
  return tokens;
}

export function logout() {
  if (typeof window === "undefined") {
    return;
  }

  window.localStorage.removeItem(ACCESS_TOKEN_KEY);
  window.localStorage.removeItem(REFRESH_TOKEN_KEY);
}

export function getAccessToken(): string | null {
  if (typeof window === "undefined") {
    return null;
  }

  return window.localStorage.getItem(ACCESS_TOKEN_KEY);
}

export function getRefreshToken(): string | null {
  if (typeof window === "undefined") {
    return null;
  }

  return window.localStorage.getItem(REFRESH_TOKEN_KEY);
}

export function getAuthHeader(): Record<string, string> {
  const token = getAccessToken();
  if (!token) {
    return {};
  }

  return { Authorization: `Bearer ${token}` };
}

function persistTokens(tokens: AuthTokens) {
  if (typeof window === "undefined") {
    return;
  }

  window.localStorage.setItem(ACCESS_TOKEN_KEY, tokens.access_token);
  if (tokens.refresh_token) {
    window.localStorage.setItem(REFRESH_TOKEN_KEY, tokens.refresh_token);
  }
}

export function isLoggedIn(): boolean {
  return Boolean(getAccessToken());
}
