## Permissions and Groups

- `Book` model defines custom permissions: `can_view`, `can_create`, `can_edit`, `can_delete`.
- Groups:
  - **Viewers** – can view only
  - **Editors** – can view, create, and edit
  - **Admins** – all permissions

To assign permissions:
1. Create groups in admin panel.
2. Assign permissions to each group.
3. Assign users to groups.
