INSERT INTO auth_user (
    id,
    password,
    last_login,
    is_superuser,
    username,
    first_name,
    last_name,
    email,
    is_staff,
    is_active,
    date_joined
  )
VALUES (
    id :int,
    'password:varchar',
    'last_login:datetime',
    'is_superuser:tinyint',
    'username:varchar',
    'first_name:varchar',
    'last_name:varchar',
    'email:varchar',
    'is_staff:tinyint',
    'is_active:tinyint',
    'date_joined:datetime'
  );