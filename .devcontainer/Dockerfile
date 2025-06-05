# Pull python image with uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install git
RUN apt update && apt upgrade -y
Run apt install -y --no-install-recommends git curl

# Set user to root
USER root

# Add bash aliases
RUN echo "alias la='ls -a'" >> /etc/bash.bashrc
RUN echo "alias ll='ls -la'" >> /etc/bash.bashrc

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

# Set the default user.
USER $USERNAME

# Set default shell
RUN sudo chsh -s /bin/bash $USERNAME

# Setup starship prompt
RUN curl -sS https://starship.rs/install.sh | sh -s -- -y
RUN printf "\n# Load starship prompt\n" >> /home/$USERNAME/.bashrc
RUN echo 'eval "$(starship init bash)"' >> /home/$USERNAME/.bashrc

