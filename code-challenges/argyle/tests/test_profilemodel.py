import profilemodel


def test_address():
    address_data = {
        'line1': '4 Jackson St',
        'line2': 'Apt C',
        'city': 'Norton',
        'state': 'MA',
        'postal_code': '27660',
        'country': 'US',
    }
    address = profilemodel.Address(**address_data)
    assert address.dict() == address_data

    del address_data['line2']
    address = profilemodel.Address(**address_data)
    # Optional 'line2'
    assert address.dict() == address_data | {'line2': None}


def test_profile():
    profile_data = {
        'id': '47b216e2-d334-4235-bc1e-185d15ab18d0',
        'account': '010db8b4-a724-47fc-a17e-733b656312a2',
        'employer': 'walmart',
        'first_name': 'John',
        'last_name': 'Smith',
        'full_name': 'John Smith',
        'email': 'john.smith@email.com',
        'phone_number': '+11234567890',
        'birth_date': None,
        'picture_url': 'https://profile.picture.com/picture.jpeg',
        'address': {
            'line1': '4 Jackson St',
            'line2': 'Apt C',
            'city': 'Norton',
            'state': 'MA',
            'postal_code': '27660',
            'country': 'US',
        },
    }
    profile = profilemodel.Profile(**profile_data)
    assert profile.dict() == profile_data

    del profile_data['account']
    del profile_data['birth_date']
    profile = profilemodel.Profile(**profile_data)
    # Optional 'account' and 'birth_date'.
    assert profile.dict() == profile_data | {'birth_date': None, 'account': None}


def test_basicprofile():
    basicprofile_data = {
        'name': 'Allainclair',
        'surname': 'Flausino dos Santos',
        'plan': 'freelance',
        'visibility': 'invisible',
        'availability': 'More than 100hrs/w',
    }
    profile = profilemodel.BasicProfile(**basicprofile_data)
    assert profile.dict() == basicprofile_data
