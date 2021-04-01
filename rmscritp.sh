#!/bin/bash

cd comments/migrations
rm -rf 00*
rm -rf __pycache__
cd ../..
echo 'Removed comments Migrations'
ls comments/migrations

cd favorite/migrations
rm -rf 00*
rm -rf __pycache__
cd ../..
echo 'Removed favorite Migrations'
ls favorite/migrations

cd location/migrations
rm -rf 00*
rm -rf __pycache__
cd ../..
echo 'Removed location Migrations'
ls location/migrations

cd users/migrations
rm -rf 00*
rm -rf __pycache__
cd ../..
echo 'Removed users Migrations'
ls users/migrations

cd visits/migrations
rm -rf 00*
rm -rf __pycache__
cd ../..
echo 'Removed visits Migrations'
ls visits/migrations

rm -rf db.sql*
echo 'Removed Database Migrations'