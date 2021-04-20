def checkLogin(users, login):
  for user in users:
    if user == login:
      return True
  return False