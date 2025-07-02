
# 🛡️ FastAPI OAuth2 Authlib Method Reference & Provider Support Matrix

This document summarizes all important methods available in `oauth.<provider>` when using **Authlib with FastAPI**, along with their usage and provider compatibility (Google, GitHub, Facebook, Microsoft, etc).

---

## 📌 Common OAuth2 Methods (Available Across Providers)

| Method | Description | Supported By |
|---|---|---|
| `authorize_redirect(request, redirect_uri)` | Redirects user to provider's OAuth authorization page. Starts OAuth flow. | ✅ All Providers |
| `authorize_access_token(request)` | Exchanges authorization code for access token after redirect back. | ✅ All Providers |
| `fetch_token(**kwargs)` | Lower-level manual token exchange (rare in FastAPI). | ✅ All Providers |
| `.get()`, `.post()`, `.put()`, `.delete()` | Makes authenticated HTTP API requests to provider using stored token. | ✅ All Providers |

---

## 📌 OpenID Connect (OIDC) Specific Methods

| Method | Description | Supported By |
|---|---|---|
| `parse_id_token(request, token)` | Parses and verifies the ID Token (JWT). Used only by OIDC providers (like Google, Microsoft). | ✅ Only OIDC providers (Google, Microsoft, Okta, Auth0, etc) |

---

## 📌 Token Refresh & Revocation

| Method | Description | Supported By |
|---|---|---|
| `refresh_token(refresh_token, **kwargs)` | Refreshes the access token using a refresh token. | ✅ Providers that support refresh tokens (Google, Microsoft, Facebook, etc) ❌ Not GitHub |
| `revoke_token(token, **kwargs)` | Revokes an existing access or refresh token. | ✅ Providers with revocation endpoint (Google, GitHub, Facebook, Microsoft, etc) |

---

## ✅ Provider Feature Support Matrix

| Provider | OIDC / ID Token | Refresh Token | Token Revocation | Scopes Example |
|---|---|---|---|---|
| **Google** | ✅ Yes | ✅ Yes | ✅ Yes | `openid`, `email`, `profile` |
| **Microsoft (Azure AD)** | ✅ Yes | ✅ Yes | ✅ Yes | `openid`, `email`, `profile` |
| **GitHub** | ❌ No | ❌ No | ✅ Yes | `user`, `repo`, `read:user` |
| **Facebook** | ❌ No | ✅ Yes (Long-Lived Tokens) | ✅ Yes | `public_profile`, `email` |
| **LinkedIn** | ❌ No | ✅ Yes | ✅ Yes | `r_liteprofile`, `r_emailaddress` |
| **Okta / Auth0** | ✅ Yes | ✅ Yes | ✅ Yes | `openid`, `email`, `profile` |

---

## ✅ Example FastAPI OAuth Flow Code (Google Example)

```python
# Step 1: Redirect to Google OAuth login
return await oauth.google.authorize_redirect(request, redirect_uri)

# Step 2: Handle callback and get access token
token = await oauth.google.authorize_access_token(request)

# Step 3: Optional: Parse ID Token (if using OpenID Connect scopes)
user_info = await oauth.google.parse_id_token(request, token)

# Step 4: Make authenticated API calls (e.g., get user profile)
response = await oauth.google.get('userinfo', token=token)
profile = response.json()
```

---

## ✅ Notes

- ✅ **`authorize_redirect`** and **`authorize_access_token`** → Work for **all OAuth2 providers**.
- ✅ **`parse_id_token`** → Only for **OpenID Connect (OIDC) providers**.
- ✅ **`refresh_token`** and **`revoke_token`** → Work **only if the provider supports** these in their OAuth spec.

---

## ✅ References

- [Authlib OAuth FastAPI Docs](https://docs.authlib.org/en/latest/client/fastapi.html)
- [Authlib Starlette OAuth Client](https://docs.authlib.org/en/latest/client/starlette.html)
- [Google OAuth2 Docs](https://developers.google.com/identity/protocols/oauth2)
- [GitHub OAuth Docs](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps)
- [Microsoft OAuth2 Docs](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)