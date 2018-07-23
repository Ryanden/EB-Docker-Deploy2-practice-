#!/usr/bin/env python

import subprocess
import os
import argparse
import sys

MODES = ['base', 'local', 'dev', 'production']


def get_mode():

    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--mode', help=f'Docker build mode{MODES}')

    args = parser.parse_args()

    # args mode 에 입력값이 있으면 공백제거, 소문자로
    if args.mode:
        mode = args.mode.strip().lower()

    else:
        while True:
            print('Select mode')
            for i, mode_name in enumerate(MODES, start=1):
                print(f' {i}. {mode_name}')
            selected_mode = input('Choice: ')

            try:
                mode_index = int(selected_mode) - 1
                mode = MODES[mode_index]
                break
            except IndexError:
                print('1~4번을 입력하세요.')
    return mode


def mode_function(mode):
    if mode in MODES:
        cur_module = sys.modules[__name__]

        getattr(cur_module, f'build_{mode}')()
    else:
        raise ValueError(f'{MODES}에 속하는 모드만 가능합니다.')


def build_base():
    try:
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
        subprocess.call('docker build -t eb-docker:base -f Dockerfile.base .', shell=True)
    finally:
        os.remove('requirements.txt')


def build_dev():
    try:
        # pipenv lock 으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements --dev > requirements.txt', shell=True)
        # docker build
        subprocess.call('docker build -t eb-docker:dev -f Dockerfile.dev .', shell=True)
    finally:
        # 끝난 후 requirements.txt 파일 삭제
        os.remove('requirements.txt')


def build_production():
    try:
        # pipenv lock 으로 requirements.txt 생성
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
        # docker build
        subprocess.call('docker build -t eb-docker:production -f Dockerfile.production .', shell=True)
    finally:
        # 끝난 후 requirements.txt 파일 삭제
        os.remove('requirements.txt')


if __name__ == '__main__':
    mode = get_mode()

    mode_function(mode)
