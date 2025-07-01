# Google API Endpoints

## Google Drive API
- **List Files**: 
  - `GET https://www.googleapis.com/drive/v3/files`
- **Get File Metadata**: 
  - `GET https://www.googleapis.com/drive/v3/files/{fileId}`
- **Create File**: 
  - `POST https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart`
- **Update File**: 
  - `PATCH https://www.googleapis.com/upload/drive/v3/files/{fileId}?uploadType=multipart`
- **Delete File**: 
  - `DELETE https://www.googleapis.com/drive/v3/files/{fileId}`

## Google Contacts API
- **List Contacts**: 
  - `GET https://people.googleapis.com/v1/people/me/connections`
- **Get Contact Details**: 
  - `GET https://people.googleapis.com/v1/people/{resourceName}`
- **Create Contact**: 
  - `POST https://people.googleapis.com/v1/people:createContact`
- **Update Contact**: 
  - `PATCH https://people.googleapis.com/v1/people/{resourceName}`
- **Delete Contact**: 
  - `DELETE https://people.googleapis.com/v1/people/{resourceName}`

## Google Calendar API
- **List Events**: 
  - `GET https://www.googleapis.com/calendar/v3/calendars/primary/events`
- **Get Event Details**: 
  - `GET https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}`
- **Create Event**: 
  - `POST https://www.googleapis.com/calendar/v3/calendars/primary/events`
- **Update Event**: 
  - `PUT https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}`
- **Delete Event**: 
  - `DELETE https://www.googleapis.com/calendar/v3/calendars/primary/events/{eventId}`

## Google People API
- **Get User Profile**: 
  - `GET https://people.googleapis.com/v1/people/me`
- **List Connections**: 
  - `GET https://people.googleapis.com/v1/people/me/connections`
- **Get Contact Details**: 
  - `GET https://people.googleapis.com/v1/people/{resourceName}`

## Google Sheets API
- **Get Spreadsheet**: 
  - `GET https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}`
- **Create Spreadsheet**: 
  - `POST https://sheets.googleapis.com/v4/spreadsheets`
- **Update Spreadsheet**: 
  - `PUT https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}`
- **Append Values**: 
  - `POST https://sheets.googleapis.com/v4/spreadsheets/{spreadsheetId}/values/{range}:append`

## Google Gmail API
- **List Messages**: 
  - `GET https://gmail.googleapis.com/gmail/v1/users/me/messages`
- **Get Message**: 
  - `GET https://gmail.googleapis.com/gmail/v1/users/me/messages/{messageId}`
- **Send Email**: 
  - `POST https://gmail.googleapis.com/gmail/v1/users/me/messages/send`
- **Delete Message**: 
  - `DELETE https://gmail.googleapis.com/gmail/v1/users/me/messages/{messageId}`

## Summary

These endpoints allow you to interact with various Google services using OAuth 2.0 for authentication. Make sure to refer to the official documentation for each API for detailed information on request parameters, response formats, and additional capabilities:

- [Google Drive API Documentation](https://developers.google.com/drive)
- [Google Contacts API Documentation](https://developers.google.com/contacts/v3)
- [Google Calendar API Documentation](https://developers.google.com/calendar)
- [Google People API Documentation](https://developers.google.com/people)
- [Google Sheets API Documentation](https://developers.google.com/sheets)
- [Google Gmail API Documentation](https://developers.google.com/gmail/api)
