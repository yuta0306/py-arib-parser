FROM ubuntu:22.04

USER root
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt-get update
RUN apt install -y sudo curl unzip vim wget git less llvm make g++ clang build-essential
RUN apt install -y autoconf automake libtool pkg-config nasm libpng-dev libfdk-aac-dev libx264-dev libx265-dev \
    libaribb24-0 libaribb24-dev libmysofa-dev libass-dev libmp3lame-dev libopus-dev \
    libtheora-dev libvorbis-dev libvpx-dev libx264-dev libx265-dev libaom-dev openssl
RUN apt install -y libgl1-mesa-dev

RUN useradd --uid 1001 --create-home --shell /bin/bash -G sudo,root arib
RUN echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /root

RUN git clone https://git.ffmpeg.org/ffmpeg.git
RUN cd ffmpeg && git checkout n6.0

RUN cd ffmpeg && ./configure --prefix=/usr        \
    --enable-gpl         \
    --enable-version3    \
    --enable-nonfree     \
    --enable-static      \
    --disable-shared     \
    --disable-debug      \
    --enable-libass      \
    --enable-libfdk-aac  \
    --enable-libfreetype \
    --enable-libmp3lame  \
    --enable-libopus     \
    --enable-libtheora   \
    --enable-libvorbis   \
    --enable-libvpx      \
    --enable-libx264     \
    --enable-libx265     \
    --enable-libaribb24  \
    --enable-libaom     \
    --docdir=/usr/share/doc/ffmpeg-6.0 && make -j \
    && gcc tools/qt-faststart.c -o tools/qt-faststart
RUN cp ffmpeg/ffmpeg ffmpeg/ffmpeg_g ffmpeg/ffprobe ffmpeg/ffprobe_g /usr/bin/

USER arib
WORKDIR /home/arib

RUN curl -sSf https://rye-up.com/get | RYE_INSTALL_OPTION="--yes" bash
RUN echo 'source "$HOME/.rye/env"' >> ~/.bashrc

CMD [ "/bin/bash" ]