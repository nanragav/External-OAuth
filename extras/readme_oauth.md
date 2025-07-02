
# 🔐 OAuth2 & OpenID Connect Integration with FastAPI + Authlib

This repository provides a **complete reference for integrating OAuth2 and OIDC** into your FastAPI applications using [Authlib](https://docs.authlib.org). It includes:
- Supported provider endpoints (Google, GitHub, Microsoft, Facebook, etc.)
- Scopes and API usage for OAuth APIs (especially Google)
- `client_kwargs` reference
- Code examples
- Authlib method overview

---

## 📌 Contents

1. [Authlib OAuth Methods Overview](#authlib-oauth-methods-overview)
2. [Provider Capabilities & Endpoint Matrix](#provider-capabilities--endpoint-matrix)
3. [OpenID Discovery URLs](#openid-discovery-urls)
4. [Google OAuth: Scopes & API Endpoints](#google-oauth-scopes--api-endpoints)
5. [General OAuth Scopes & API References](#general-oauth-scopes--api-references)
6. [Client_kwargs Parameters Reference](#client_kwargs-parameters-reference)
7. [Helpful Links](#helpful-links)

---

## ✅ Authlib OAuth Methods Overview

| Method | Description | Providers |
|--------|-------------|-----------|
| `authorize_redirect(request, redirect_uri)` | Start the OAuth2 login by redirecting the user | ✅ All |
| `authorize_access_token(request)` | Exchange code for token | ✅ All |
| `.get()`, `.post()` etc. | Make authenticated API calls with token | ✅ All |
| `parse_id_token(request, token)` | Decode OIDC ID token (JWT) | ✅ OIDC providers only |
| `refresh_token(refresh_token)` | Refresh access token | ✅ Google, Microsoft, Facebook, LinkedIn |
| `revoke_token(token)` | Revoke token | ✅ Most (except Twitter, some GitHub flows) |

🧩 See full matrix in [`authlib_oauth_methods.md`](./authlib_oauth_methods.md)

---

## 🌐 Provider Capabilities & Endpoint Matrix

See complete provider references and tested URLs here:
- [`oauth2_providers_url.md`](./oauth2_providers_url.md)
- [`openid_url.md`](./openid_url.md)

Examples:

### Google OAuth2
- Discovery: [accounts.google.com](https://accounts.google.com/.well-known/openid-configuration)
- Auth URL: `https://accounts.google.com/o/oauth2/v2/auth`
- Token URL: `https://oauth2.googleapis.com/token`
- User Info: `https://openidconnect.googleapis.com/v1/userinfo`

### GitHub OAuth2
- Auth URL: `https://github.com/login/oauth/authorize`
- Token URL: `https://github.com/login/oauth/access_token`
- User API: `https://api.github.com/user`

More in [`oauth2_providers_url.md`](./oauth2_providers_url.md)

---

## 🔍 OpenID Discovery URLs

See [`openid_url.md`](./openid_url.md) for a comprehensive list of `.well-known/openid-configuration` links for:

- Google
- Microsoft Azure AD
- Apple
- Okta
- Auth0
- Keycloak
- Amazon Cognito
- Ping Identity
- OneLogin
- Salesforce
- Many more...

---

## 🔑 Google OAuth: Scopes & API Endpoints

See:
- [`google_api_scopes.md`](./google_api_scopes.md)
- [`google_api_endpoints.md`](./google_api_endpoints.md)

### Example Scopes

| Service | Scope |
|--------|-------|
| Drive Full Access | `https://www.googleapis.com/auth/drive` |
| Contacts ReadOnly | `https://www.googleapis.com/auth/contacts.readonly` |
| Calendar Events | `https://www.googleapis.com/auth/calendar` |
| Sheets Read/Write | `https://www.googleapis.com/auth/spreadsheets` |
| Gmail Send Email | `https://www.googleapis.com/auth/gmail.send` |

### Example API Endpoints

| API | Endpoint |
|-----|----------|
| List Drive Files | `GET https://www.googleapis.com/drive/v3/files` |
| Create Calendar Event | `POST https://www.googleapis.com/calendar/v3/calendars/primary/events` |
| Send Email via Gmail | `POST https://gmail.googleapis.com/gmail/v1/users/me/messages/send` |

---

## 🌍 General OAuth Scopes & API References

See [`general_oauth_scopes_and_api_endpoints.md`](./general_oauth_scopes_and_api_endpoints.md)

Supported platforms:
- Google
- Facebook
- GitHub
- Microsoft Graph
- Twitter

Each includes:
- Common OAuth scopes
- Direct API links
- REST endpoint patterns

---

## ⚙️ client_kwargs Parameters Reference

See [`client_kwargs_parameters.md`](./client_kwargs_parameters.md)

Useful when configuring `oauth.register()` in FastAPI:

```python
oauth.register(
    name="google",
    client_id="...",
    client_secret="...",
    server_metadata_url="...",
    client_kwargs={
        "scope": "openid email profile",
        "prompt": "consent",
        "access_type": "offline",
        "include_granted_scopes": "true"
    }
)
```

Key parameters:
- `scope`, `prompt`, `access_type`
- `response_type`, `nonce`, `state`
- `code_challenge`, `code_challenge_method`

---

## 🔗 Helpful Links

- [Authlib FastAPI Docs](https://docs.authlib.org/en/latest/client/fastapi.html)
- [Google OAuth2 Docs](https://developers.google.com/identity/protocols/oauth2)
- [Microsoft Identity Docs](https://learn.microsoft.com/en-us/azure/active-directory/develop/)
- [GitHub OAuth Guide](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps)
- [Facebook Graph API](https://developers.facebook.com/docs/graph-api)
- [Twitter API Docs](https://developer.twitter.com/en/docs/twitter-api)

---

## 📁 Included Files

| File | Description |
|------|-------------|
| `authlib_oauth_methods.md` | Authlib methods + provider matrix |
| `oauth2_providers_url.md` | Endpoints for Google, GitHub, Facebook, etc. |
| `openid_url.md` | Discovery URLs for OIDC providers |
| `google_api_scopes.md` | Google API scopes by product |
| `google_api_endpoints.md` | REST endpoints for Google APIs |
| `general_oauth_scopes_and_api_endpoints.md` | Scopes + APIs for other providers |
| `client_kwargs_parameters.md` | Guide to `client_kwargs` fields in Authlib |

---

## 📣 Contributing

Feel free to open issues or PRs for:
- Additional provider support
- Updated scopes or endpoints
- Authlib/FastAPI implementation tips

---

## 📝 License

This documentation is open-source and available under the [MIT License](LICENSE).
