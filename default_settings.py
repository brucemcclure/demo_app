import os                                                           # Operating System package used to retrieve env variables

class Config(object):
    JWT_SECRET_KEY = "Dev Key"                                      # Key used for development
    SQLALCHEMY_TRACK_MODIFICATIONS = False                          # Documentaion says this should be false unless needed
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024                            # Max size for file uplaod

    @property
    def SQLALCHEMY_DATABASE_URI(self):                              # This is a function that will be used for all envs
        value = os.environ.get("DB_URI")                            # Retrieve the DB_URI from the .env file to connect to DB
        if not value:
            raise ValueError("SQLALCHEMY_DATABASE_URI is not set")  # Raise error if it is not set
        return value    


    @property
    def AWS_ACCESS_KEY_ID(self):                                    # This is a function that will be used for all envs
        value = os.environ.get("AWS_ACCESS_KEY_ID")                 # Retrieve the AWS_ACCESS_KEY_ID for IAM from the .env file.
        if not value:
            raise ValueError("AWS_ACCESS_KEY_ID is not set")        # Raise error if it is not set
        return value


    @property
    def AWS_SECRET_ACCESS_KEY(self):                                # This is a function that will be used for all envs
        value = os.environ.get("AWS_SECRET_ACCESS_KEY")             # Retrieve the AWS_SECRET_ACCESS_KEY for IAM from the .env file.
        if not value:
            raise ValueError("AWS_SECRET_ACCESS_KEY is not set")    # Raise error if it is not set
        return value


    @property
    def AWS_S3_BUCKET(self):                                        # This is a function that will be used for all envs
        value = os.environ.get("AWS_S3_BUCKET")                     # Retrieve the AWS_S3_BUCKET for IAM from the .env file.
        if not value:
            raise ValueError("AWS_S3_BUCKET is not set")            # Raise error if it is not set
        return value