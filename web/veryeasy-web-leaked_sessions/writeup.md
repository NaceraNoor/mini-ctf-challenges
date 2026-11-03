# web-easy-leaked-sessions

**Category:** Web | **Difficulty:** very easy
**Flag:** `shellmates{9571c5bd902f38d46662cdd2fb}`

## Challenge
Players register an account, log in, and land on their profile page, which
includes a "Session Info" feature.

## Vulnerability
The server identifies a logged-in user purely by the value of the
`session_id` cookie, checked against a server-side mapping of
`session_id -> username`. This is standard session design — but the
"Session Info" page leaks the full contents of that mapping to *any*
logged-in user, not just their own entry:

    session_id -> username
    a1b2c3...  -> alice
    d4e5f6...  -> admin

Since the admin account is active on the server from startup, its
session_id is present in this list the moment a player visits the page.
Because the server trusts the `session_id` cookie alone, with no additional
binding (no IP check, no user-agent check, no rotation), whoever presents
that value *is* that user — a classic bearer-token session design with no
authorization logic around who can see which sessions.

## Solution
1. Register an account and log in.
2. From the profile page, click "Session Info" to view the list of active
   sessions. Note the `session_id` value listed next to `admin`.
3. Open DevTools (right-click → Inspect, or F12), go to the **Application**
   tab → **Cookies**, and find the `session_id` cookie for the site.
4. Replace its value with the admin's leaked `session_id`.
5. Reload the page (`/`). The server now resolves your cookie to the admin
   account, and the flag is displayed on the profile page.

## Note
No solve script is provided — the intended solve path is fully manual,
using only the browser and DevTools.