from .. import models
import transaction

if __name__ == '__main__':
    models.Base.metadata.create_all(models.engine)
    with transaction.manager:
        notification = models.Notification(
            title='My test',
            msg='Message of the notification'
        )
        models.DBSession.add(notification)
