#!/usr/bin/env bash
CURRENT_PATH=`pwd`

export FLASK_CONFIG="default"
export SECRET_KEY="!@#$%^&*"
export DEV_DATABASE_URL="mysql://root:123456@127.0.0.1/bgs"
export FLASK_LOGGING_CONF=$CURRENT_PATH/logging.yml