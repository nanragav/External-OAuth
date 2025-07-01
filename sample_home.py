@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = request.session.get("user")
    drive_files = request.session.get("drive_files", [])
    contacts = request.session.get("contacts", [])

    if user:
        drive_files_list = "".join(f"<li>{file['name']}</li>" for file in drive_files)
        contacts_list = "".join(f"<li>{contact.get('names', [{}])[0].get('displayName', 'No Name')}</li>" for contact in contacts)

        return f"""
            <h1>Welcome {user['name']}</h1>
            <p>Email: {user['email']}</p>
            <h2>Your Drive Files:</h2>
            <ul>{drive_files_list}</ul>
            <h2>Your Contacts:</h2>
            <ul>{contacts_list}</ul>
            <a href='/logout'>Logout</a>
        """
    return "<a href='/login'>Login with Google</a>"
