FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Update container
RUN apt update && apt upgrade -y

# Set user to root
USER root

# Create non-root user 'dev'
ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Set the working directory
WORKDIR /home/${USERNAME}

# Set the default user.
USER $USERNAME

# Set default shell
RUN sudo chsh -s /bin/bash $USERNAME

# Create a python virtual environment using uv
RUN uv venv /home/$USERNAME/venv --seed
# Use the virtual environment automatically
ENV VIRTUAL_ENV=/home/$USERNAME/venv
# Place entry points in the environment at the front of the path
ENV PATH="/home/$USERNAME/venv/bin:/home/$USERNAME/.local/bin:$PATH"

# Install JupyterLab and other dependencies using uv
RUN uv pip install jupyterlab

# Expose the Jupyter port
EXPOSE 8888

# Command to run JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token='rs'"]
