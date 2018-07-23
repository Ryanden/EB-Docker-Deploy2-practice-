FROM            ryanden/fc-8th-eb-docker:base

MAINTAINER      lockstom3@gmail.com

ENV             PROJECT_DIR             /srv/project
ENV             BUILD_MODE              production
ENV             DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY            .   ${PROJECT_DIR}
RUN             mkdir   /var/log/django

# Nginx 설정파일을 복사
RUN             cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/nginx.conf/etc/nginx/nginx.conf && \

# available에 있는 파일 복사
                cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/nginx_app.conf/etc/nginx/site-available && \

# 링크 연결
                ln -sf  /etc/nginx/site-available/nginx_app.conf/etc/nginx/sites-enabled

# supervisor 설정 복사
RUN             cp -f   ${PROJECT_DIR}/.config/${BUILD_MODE}/supervisor_app.conf/etc/supervisor/conf.d/

EXPOSE          80

CMD             supervisord -n