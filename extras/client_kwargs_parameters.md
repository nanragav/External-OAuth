# Client_kwargs Parameters for OAuth 2.0 and OpenID Connect

In the context of OAuth 2.0 and OpenID Connect, the `client_kwargs` parameter is used to pass additional parameters to the OAuth client when making requests. Below are common parameters that can be included in `client_kwargs`:

| Parameter               | Description                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------|
| **scope**               | Specifies the permissions the application is requesting. Common scopes include `openid`, `profile`, `email`, etc. |
| **redirect_uri**        | The URI to which the authorization server will redirect the user after authorization.        |
| **response_type**       | Indicates the type of response expected from the authorization server. Common values are `code` (for authorization code flow) and `token` (for implicit flow). |
| **state**               | A unique string used to maintain state between the request and callback, helping to prevent CSRF attacks. |
| **nonce**               | A string used to associate a client session with an ID token, helping to mitigate replay attacks. |
| **prompt**              | Specifies how the authorization server should prompt the user for re-authentication. Common values include `login`, `consent`, and `none`. |
| **max_age**             | Specifies the maximum allowable age of the authentication session. If the session is older than this value, the user will be prompted to re-authenticate. |
| **ui_locales**          | A comma-separated list of language tags that the authorization server can use to localize the user interface. |
| **login_hint**          | A hint about the user's identity, such as their email address, to pre-fill the login form.   |
| **client_id**           | The unique identifier for the client application, although this is often set when initializing the client. |
| **client_secret**       | The secret associated with the client ID, typically used in confidential client flows.        |
| **code_challenge**      | Used in the PKCE (Proof Key for Code Exchange) flow to enhance security.                     |
| **code_challenge_method**| Specifies the method used to generate the `code_challenge`, typically `S256` for SHA-256.  |
| **access_type**         | Used in some providers (like Google) to specify whether the access token should be short-lived or long-lived (e.g., `offline` for refresh tokens). |
| **include_granted_scopes** | A boolean parameter that indicates whether to include previously granted scopes in the authorization request. |

These parameters can help customize the behavior of the OAuth flow and enhance security. Always refer to the specific documentation of the OAuth provider you are working with, as they may have additional or different parameters.
