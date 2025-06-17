import aioboto3
from fastapi import APIRouter, Body, UploadFile

ACCESS_KEY = '84c2e18ac678c20ceac03aa287b38efc'
SECRET_KEY = '53edc2131d4eb7f41d617ed8dc99aaae59e5ff6ee179c97c59462fbe64557a76'
BUCKET_NAME = 'group25022025'
ENDPOINT = 'https://0384693236a813fcae8b79609af758d0.r2.cloudflarestorage.com/group25022025'
PUBLIC_URL = 'https://pub-83b871a11ef249a180c01e65e3c11b56.r2.dev'


class  S3Storage:
    def __init__(self):
        self.bucket_name = BUCKET_NAME

    async def get_s3_session(self):
        session = aioboto3.Session()
        async with session.client(
            's3',
            endpoint_url=ENDPOINT,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            region_name='EEUR'
        ) as s3:
            yield s3

    async def upload_product_image(self, file: UploadFile, product_uuid: str) -> str:
        async for s3_client in self.get_s3_session():
            path = f'products/{product_uuid}/{file.filename}'
            await s3_client.upload_fileobj(file, self.bucket_name, path)
            url = f"{PUBLIC_URL}/{path}"
        return url


s3_storage = S3Storage()