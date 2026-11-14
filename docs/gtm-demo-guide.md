# Sales demo guide (owner: GTM team)

Use this on customer calls to show how leads get into Leadly.

1. Add a lead:
   `curl -X POST http://localhost:8000/v8/leads -H "Content-Type: application/json" -d '{"full_name": "Asha", "work_email": "asha@example.com"}'`
   Expected: the new lead comes back with an "id".
2. Show all leads:
   `curl http://localhost:8000/v8/leads`
   Expected: Asha is in the list.
