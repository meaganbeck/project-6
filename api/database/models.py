from mongoengine import *


class Checkpoint(EmbeddedDocument):
    """
    A MongoEngine EmbeddedDocument containing:
        distance: MongoEngine float field, required, (checkpoint distance in kilometers),
		location: MongoEngine string field, optional, (checkpoint location name),
		open_time: MongoEngine datetime field, required, (checkpoint opening time),
		close_time: MongoEngine datetime field, required, (checkpoint closing time).
    """
    #d = FloatField(required = True)
    #miles = FloatField(required = True)
    distance = FloatField(required = True)
    location = StringField(required = False)
    open_time = DateTimeField(required = True)
    close_time = DateTimeField(required = True)


class Brevet(Document):
    """

    A MongoEngine document containing:
		length: MongoEngine float field, required
		start_time: MongoEngine datetime field, required
		checkpoints: MongoEngine list field of Checkpoints, required
    """
    brevet_dist = FloatField(required = True)
    start_time = DateTimeField(required = True)
    checkpoints = EmbeddedDocumentListField(Checkpoint, required=True)
