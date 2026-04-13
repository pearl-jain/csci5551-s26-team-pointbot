# Start from ROS Jazzy with perception packages
FROM osrf/ros:jazzy-desktop

# --- User setup ---
# These are overridden by devcontainer.json args
# --- User setup ---
ARG USERNAME=adam
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 1. Clean up existing users with the same UID/GID to avoid conflicts
RUN if id -u $USER_UID >/dev/null 2>&1; then userdel -f $(id -un $USER_UID); fi \
    && if getent group $USER_GID >/dev/null 2>&1; then groupdel $(getent group $USER_GID | cut -d: -f1); fi

# 2. Create user and configure passwordless sudo
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update && apt-get install -y sudo \
    && mkdir -p /etc/sudoers.d \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# --- System updates & core tools ---
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    python3-pip \
    curl \
    lsb-release \
    gnupg \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# --- GUI / Qt deps (Generalized for Wayland/X11) ---
RUN apt-get update && apt-get install -y \
    libqt5gui5 \
    libqt5core5a \
    libqt5widgets5 \
    qtwayland5 \
    libxkbcommon-x11-0 \
    x11-apps \
    mesa-utils \
    libgl1-mesa-dri \
    v4l-utils \
    libv4l-dev \
    libopencv-videoio-dev \
    && rm -rf /var/lib/apt/lists/*
    
# --- Gazebo (gz-harmonic) install ---
RUN curl -fsSL https://packages.osrfoundation.org/gazebo.gpg \
        -o /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] \
        https://packages.osrfoundation.org/gazebo/ubuntu-stable noble main" \
        > /etc/apt/sources.list.d/gazebo-stable.list \
    && apt-get update \
    && apt-get install -y gz-harmonic ros-jazzy-ros-gz \
    && rm -rf /var/lib/apt/lists/*

# --- ROS2 packages + SLAM dependencies ---
RUN apt-get update && apt-get install -y \
    ros-jazzy-turtlesim \
    ros-jazzy-cv-bridge \
    ros-jazzy-tf2-ros \
    ros-jazzy-slam-toolbox \
    ros-jazzy-webots-ros2 \
    ros-jazzy-moveit \
    ros-jazzy-moveit-py \
    && rm -rf /var/lib/apt/lists/*

# --- Environment variables ---
ENV SHELL=/bin/bash
ENV QT_X11_NO_MITSHM=1

# --- Automatically source ROS 2 and Gazebo for the user ---
RUN echo "source /opt/ros/jazzy/setup.bash" >> /home/$USERNAME/.bashrc \
    && echo "source /usr/share/gz/gz_harmonic/setup.sh" >> /home/$USERNAME/.bashrc \
    && echo "if [ -f /home/$USERNAME/ws/install/setup.bash ]; then source /home/$USERNAME/ws/install/setup.bash; fi" >> /home/$USERNAME/.bashrc

# --- Set default user ---
USER $USERNAME
WORKDIR /home/$USERNAME/point_bot_ws

CMD ["/bin/bash"]