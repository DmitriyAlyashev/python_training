from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(contact_firstname="Peter", contact_lastname="Shteiman", contact_address="Russia"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(contact_firstname="", contact_lastname="", contact_address=""))
    app.session.logout()
