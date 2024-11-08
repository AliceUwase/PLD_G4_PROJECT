from Freelance_job_manager.auth.authentication import authenticate_user


def test_authenticate_user_valid_credentials():
    assert authenticate_user("admin", "password") == True

def test_authenticate_user_invalid_username():
    assert authenticate_user("wrong_user", "password") == False