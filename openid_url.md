# OpenID Connect Discovery URLs for Top OAuth Providers

This list provides the server metadata (discovery) URLs for popular OAuth and OpenID Connect (OIDC) identity providers. These URLs are used to automatically discover configuration endpoints for authentication workflows in applications.

| Provider                  | Discovery URL (server_metadata_url)                                                        | Notes                                            |
|---------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------|
| **Google**                | [https://accounts.google.com/.well-known/openid-configuration](https://accounts.google.com/.well-known/openid-configuration)                               | Use for Google login                             |
| **Microsoft (Azure AD)**  | [https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration](https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration)             | Replace `common` with your tenant ID if needed   |
| **Facebook**              | Not supported                                                                              | OAuth only. Configure manually.                 |
| **GitHub**                | Not supported                                                                              | OAuth only. Configure manually.                 |
| **Apple**                 | [https://appleid.apple.com/.well-known/openid-configuration](https://appleid.apple.com/.well-known/openid-configuration)                                 | Only supports OpenID (with special client setup) |
| **Auth0**                 | [https://<YOUR_DOMAIN>/.well-known/openid-configuration](https://<YOUR_DOMAIN>/.well-known/openid-configuration)                                     | Replace `<YOUR_DOMAIN>` with your Auth0 domain   |
| **Okta**                  | [https://<YOUR_OKTA_DOMAIN>/oauth2/default/.well-known/openid-configuration](https://<YOUR_OKTA_DOMAIN>/oauth2/default/.well-known/openid-configuration)                | Replace with your Okta org URL                   |
| **Keycloak**              | [https://<YOUR_KEYCLOAK_DOMAIN>/realms/<REALM_NAME>/.well-known/openid-configuration](https://<YOUR_KEYCLOAK_DOMAIN>/realms/<REALM_NAME>/.well-known/openid-configuration)            | Replace domain and realm                         |
| **Amazon Cognito**        | [https://cognito-idp.<region>.amazonaws.com/<userPoolId>/.well-known/openid-configuration](https://cognito-idp.<region>.amazonaws.com/<userPoolId>/.well-known/openid-configuration)   | Replace with your AWS region and userPoolId      |
| **Ping Identity**         | [https://<ENVIRONMENT>/as/.well-known/openid-configuration](https://<ENVIRONMENT>/as/.well-known/openid-configuration)                                  | Replace with your Ping instance                  |
| **OneLogin**              | [https://<YOUR_SUBDOMAIN>.onelogin.com/oidc/2/.well-known/openid-configuration](https://<YOUR_SUBDOMAIN>.onelogin.com/oidc/2/.well-known/openid-configuration)              | OIDC v2                                          |
| **Salesforce**            | [https://login.salesforce.com/.well-known/openid-configuration](https://login.salesforce.com/.well-known/openid-configuration)                              | Replace with custom domain if needed             |
| **LinkedIn**              | Not supported                                                                              | OAuth 2.0 only. Manual config required           |
| **Slack**                 | Not supported                                                                              | OAuth 2.0 only. Manual config required           |
| **Red Hat SSO (RH-SSO)**  | [https://<RHSSO_DOMAIN>/auth/realms/<REALM_NAME>/.well-known/openid-configuration](https://<RHSSO_DOMAIN>/auth/realms/<REALM_NAME>/.well-known/openid-configuration)           | Built on Keycloak                                |
| **IBM Cloud App ID**      | [https://<REGION>.appid.cloud.ibm.com/oauth/v4/<TENANT_ID>/.well-known/openid-configuration](https://<REGION>.appid.cloud.ibm.com/oauth/v4/<TENANT_ID>/.well-known/openid-configuration)| Replace with IBM region and tenant ID            |
| **ForgeRock**             | [https://<FORGEROCK_DOMAIN>/oauth2/.well-known/openid-configuration](https://<FORGEROCK_DOMAIN>/oauth2/.well-known/openid-configuration)                         | Full OIDC support                                |
| **NetIQ**                 | [https://<DOMAIN>/nidp/oauth/.well-known/openid-configuration](https://<DOMAIN>/nidp/oauth/.well-known/openid-configuration)                               | Enterprise identity provider                     |
| **Bitbucket (Atlassian)** | Not supported                                                                              | OAuth 2.0 only                                   |

