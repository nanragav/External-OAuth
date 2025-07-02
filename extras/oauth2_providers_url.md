
# 🌐 OAuth2 + FastAPI + Authlib — Provider Endpoint Reference

This guide lists **detailed, real-world OAuth2 and OpenID Connect endpoints** for major providers (Google, GitHub, Microsoft, Facebook, etc.), specifically for use with **Authlib + FastAPI**.

---

## 🧠 How Authlib Uses These URLs

Authlib handles most of the heavy lifting — like redirecting to the auth page or exchanging tokens. But **you often still need raw API URLs** to:
- Fetch user info
- Revoke tokens
- Refresh access tokens
- Access additional profile info

---

## 🔍 OIDC Discovery: Universal Method for OIDC Providers

OIDC providers (Google, Microsoft, Auth0, Okta, etc.) expose a discovery document at:

```
https://<provider>/.well-known/openid-configuration
```

This will return a JSON object with endpoints like:
- `authorization_endpoint`
- `token_endpoint`
- `userinfo_endpoint`
- `jwks_uri`
- `revocation_endpoint`
- `end_session_endpoint`

You can fetch it like this:

```python
import httpx

async def fetch_metadata(provider_url):
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{provider_url}/.well-known/openid-configuration")
        return resp.json()
```

---

## ✅ Google OAuth2 + OpenID

- **OIDC Metadata**: [https://accounts.google.com/.well-known/openid-configuration](https://accounts.google.com/.well-known/openid-configuration)
- **Auth URL**: `https://accounts.google.com/o/oauth2/v2/auth`
- **Token URL**: `https://oauth2.googleapis.com/token`
- **User Info**: `https://openidconnect.googleapis.com/v1/userinfo`
- **Revoke Token**: `https://oauth2.googleapis.com/revoke`
- **Scopes**: `openid`, `email`, `profile`

### Example user info call
```python
response = await client.get(
    "https://openidconnect.googleapis.com/v1/userinfo",
    headers={"Authorization": f"Bearer {token['access_token']}"}
)
```

---

## ✅ GitHub OAuth2

- **Auth URL**: `https://github.com/login/oauth/authorize`
- **Token URL**: `https://github.com/login/oauth/access_token`
- **User Info**: `https://api.github.com/user`
- **Emails**: `https://api.github.com/user/emails`
- **Revoke Token**: GitHub does not provide a direct endpoint. Use API to delete token manually.

### Example user info call
```python
response = await client.get(
    "https://api.github.com/user",
    headers={"Authorization": f"Bearer {token['access_token']}"}
)
```

---

## ✅ Microsoft Azure AD (v2.0 Endpoint)

- **OIDC Metadata**: `https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration`
- **Auth URL**: `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize`
- **Token URL**: `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`
- **User Info**: `https://graph.microsoft.com/oidc/userinfo`
- **Graph API Profile**: `https://graph.microsoft.com/v1.0/me`
- **Scopes**: `openid`, `email`, `profile`, `User.Read`

---

## ✅ Facebook OAuth2

- **Auth URL**: `https://www.facebook.com/v15.0/dialog/oauth`
- **Token URL**: `https://graph.facebook.com/v15.0/oauth/access_token`
- **User Info**: `https://graph.facebook.com/me?fields=id,name,email`
- **Debug Token**: `https://graph.facebook.com/debug_token`
- **Revoke/Logout**: No direct revoke. Users must remove your app manually.
- **Scopes**: `email`, `public_profile`

---

## ✅ LinkedIn OAuth2

- **Auth URL**: `https://www.linkedin.com/oauth/v2/authorization`
- **Token URL**: `https://www.linkedin.com/oauth/v2/accessToken`
- **User Info**: `https://api.linkedin.com/v2/me`
- **Email Info**: `https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))`
- **Scopes**: `r_liteprofile`, `r_emailaddress`

---

## ✅ Auth0

- **Metadata URL**: `https://<your-domain>.auth0.com/.well-known/openid-configuration`
- **User Info**: `https://<your-domain>.auth0.com/userinfo`
- **Token URL**: `https://<your-domain>.auth0.com/oauth/token`
- **Logout**: `https://<your-domain>.auth0.com/v2/logout`

Replace `<your-domain>` with your actual Auth0 tenant domain.

---

## ✅ Okta

- **Metadata URL**: `https://<your-okta-domain>/oauth2/default/.well-known/openid-configuration`
- **User Info**: `https://<your-okta-domain>/oauth2/default/v1/userinfo`
- **Token URL**: `https://<your-okta-domain>/oauth2/default/v1/token`
- **Logout**: `https://<your-okta-domain>/oauth2/default/v1/logout`

---

## 📌 Final Notes

- For OIDC providers, always check `.well-known/openid-configuration` first.
- Some endpoints (like revoke) might not be exposed directly by the provider.
- Always read provider-specific docs to know what scopes are required.

---
