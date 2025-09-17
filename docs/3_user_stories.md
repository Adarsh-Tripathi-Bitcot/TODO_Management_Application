# 3. User Stories & Acceptance Criteria

We model user interactions as **scenarios**.  
Each scenario includes strict **acceptance criteria** for test-driven development.

---

## 3.1 Registration
- Scenario: New user registers.
- Acceptance:
  - Valid email/password (≥8 chars, 1 uppercase, 1 lowercase, 1 digit).
  - Unique email → 400 for duplicates.
  - Invalid email/password → 400.
  - Missing fields → 422.
  - Success: 201 status with user ID and message.

## 3.2 Login
- Valid credentials → 200 with JWT token & user metadata.
- Invalid credentials → 401 unauthorized.
- Missing fields → 422.

## 3.3 Create TODO
- Authenticated user adds a TODO.
- Required: title; optional: due_date.
- Status must be one of: todo / in progress / completed.
- Success: 201 status with new TODO ID.
- Invalid status → 400.

## 3.4 List/Read TODOs
- Returns only the user’s TODOs.
- Paginated with default limit 20.
- Sorted by created_at descending.
- Success: 200 with list.

## 3.5 Update TODO
- Only owner can update.
- Valid status enforced.
- Success: 200 updated record.
- Not found → 404.

## 3.6 Delete TODO
- Only owner can delete.
- Success: 204 no content.
- Not found → 404.

---

These stories will drive **pytest test cases** and form the basis of automated acceptance testing.
