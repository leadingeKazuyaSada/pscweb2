# pscweb2

## Repository

- [https://github.com/satamame/pscweb2](https://github.com/satamame/pscweb2)

## Overview

演劇の稽古のプランを立てるための Web アプリです。
完成度としては、最低限の基本機能はできたかな、といったところです。

## Features

- 「公演」という単位で稽古を管理します。
- シーン、登場人物、出番といったデータを入力し、香盤表を表示できます。
- これらのデータは台本 (Fountain 形式) から生成することもできます。
- 配役、役者、稽古日、出欠のデータを入力し、スケジュールを可視化します。
- いつ、どのシーンが稽古できるかの目安となる「出席率グラフ」を表示します。

## Demo

- [https://pscweb2.herokuapp.com/](https://pscweb2.herokuapp.com/)
- 自由に触っていただいて大丈夫ですが、入力したデータの消失や漏洩については責任を負いかねます。
- 無料の DB を使っているので、データが大きくなると動かなくなります。
- [使い方はこちら](demo_help/index.md)。

## Development

- Python 3.8.1
- Django 3.0.7
- Heroku free dynos
- [今後実装したい機能など](todo.md)
