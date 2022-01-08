import json
from datetime import datetime
import os

import djclick as click
from django.conf import settings

from api.models import Product, CustomUser


@click.group()
def cli():
    pass


@cli.command()
def get_products():
    """Get test data into db"""
    click.secho(f"{settings.APP_NAME}: getting products from db", fg='green')
    products = Product.objects.all()
    if len(products) == 0:
        click.secho("No products found", fg='red')
        return
    for product in products:
        click.secho(f"{product} is a good product", fg='green')


@cli.command()
def populate_products():
    """Add test data into db"""
    click.secho(f"{settings.APP_NAME}: adding products to db", fg='blue')
    with open('api/fixtures/products.json', 'r') as f:
        products = json.load(f)
        user = CustomUser.objects.get(id=1)
        for prod in products:
            product = Product(
                user = user,
                name=prod['fields'].get('name'),
                image=prod['fields'].get('image'),
                description=prod['fields'].get('description'),
                price=float(prod['fields'].get('price')),
                num_in_stock=int(prod['fields'].get('count_in_stock'))
            )
            product.save()
    click.secho(f"{len(products)} products added succesfully", fg='green')


@cli.command()
def delete_products():
    """Delete all products from db"""
    click.secho("Attempting to delete all products from db", fg='red')
    products = Product.objects.all()
    products.delete()
    click.secho("Products were successfully deleted", fg='green')
    