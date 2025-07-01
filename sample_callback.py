@app.get("/auth/google/callback")
async def auth(request: Request):
    token = await oauth.google.authorize_access_token(request)

    # Manually fetch user info from Google's endpoint
    async with httpx.AsyncClient() as client:
        # Fetch user info
        resp = await client.get(
            "https://openidconnect.googleapis.com/v1/userinfo",
            headers={"Authorization": f"Bearer {token['access_token']}"}
        )
        user = resp.json()

        # Fetch Google Drive files
        drive_resp = await client.get(
            "https://www.googleapis.com/drive/v3/files",
            headers={"Authorization": f"Bearer {token['access_token']}"}
        )
        drive_files = drive_resp.json().get('files', [])

        # Fetch Google Contacts
        contacts_resp = await client.get(
            "https://people.googleapis.com/v1/people/me/connections",
            headers={"Authorization": f"Bearer {token['access_token']}"}
        )
        contacts = contacts_resp.json().get('connections', [])

    request.session["user"] = user
    request.session["drive_files"] = drive_files
    request.session["contacts"] = contacts
    return RedirectResponse(url="/")
