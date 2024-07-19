from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Leo', email='teste@leo.com', password='senha123trocar'
    )
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'teste@leo.com'))

    assert result.username == 'Leo'
