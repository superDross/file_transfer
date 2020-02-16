import uuid

from file_transfer_tool.models import Files


def generate_unique_id(all_uids=[f.link for f in Files.objects.all()]):
    """
    Generates a unique file id not present in the db
    """
    uid = uuid.uuid1()
    if uid in all_uids:
        return generate_unique_id(all_uids)
    return uuid
