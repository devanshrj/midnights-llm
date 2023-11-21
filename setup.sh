ENV_NAME=vllm

# check if CONDA_HOME is set and create environment
if [ -z "$CONDA_HOME" ]
then
    echo "Please set CONDA_HOME to the location of your conda installation"
    exit 1
fi

# source ${CONDA_HOME}/etc/profile.d/conda.sh
# conda create -y -n ${ENV_NAME} python=3.8
# conda activate ${ENV_NAME}
# pip install -r requirements.txt