def create_contact(db, contact, user_id):
    """
    Create a new contact.

    :param db: Database session
    :param contact: Contact data
    :param user_id: Owner ID
    :return: Created contact object
    """
    obj = Contact(**contact.dict(), user_id=user_id)
    db.add(obj)
    db.commit()
    return obj
