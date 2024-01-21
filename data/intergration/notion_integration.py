# ====================================================================================
# Script Name: notion_integration.py
# Description: This script allows for the integration of Notion with the Eco-Bot application.
# Location: data\integration\notion_integration.py
# Company: KindaHelpfulMachines, KHM Smart Build
# Author: Kyle Morgan
# Version: 1.0
# Date: 15-01-2024
# Copyright: KHMSmartBuild
# ====================================================================================
"""
This script allows for the integration of Notion with the Eco-Bot application.
"""
import requests

def read_from_notion(page_id, auth_token):
    base_url = 'https://api.notion.com/v1/'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json',
        'Notion-Version': '2021-08-16'
    }
    try:
        response = requests.get(f'{base_url}pages/{page_id}', headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Error fetching data from Notion: {e}')
        return None

def write_to_notion(page_id, data, auth_token):
    base_url = 'https://api.notion.com/v1/'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json',
        'Notion-Version': '2021-08-16'
    }
    try:
        response = requests.patch(f'{base_url}pages/{page_id}', headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f'Error fetching data from Notion: {e}')
        return None
    
def get_page_id(page_url):
    page_id = page_url.split('/')[-1]
    return page_id

def get_page_url(page_id):
    page_url = f'https://www.notion.so/{page_id}'
    return page_url

def get_page_title(page_id, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        return page_data['properties']['title']['title'][0]['plain_text']
    else:
        return None
    
def get_page_content(page_id, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        return page_data['properties']['content']['rich_text'][0]['plain_text']
    else:
        return None
    
def update_page_content(page_id, new_content, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        page_data['properties']['content']['rich_text'][0]['plain_text'] = new_content
        write_to_notion(page_id, page_data, auth_token)

def get_page_tags(page_id, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        return page_data['properties']['tags']['multi_select']
    else:
        return None
    
def update_page_tags(page_id, new_tags, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        page_data['properties']['tags']['multi_select'] = new_tags
        write_to_notion(page_id, page_data, auth_token)
    else:
        print('Page not found')

def get_page_status(page_id, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        return page_data['properties']['status']['select']['name']
    else:
        return None
    
def update_page_status(page_id, new_status, auth_token):
    page_data = read_from_notion(page_id, auth_token)
    if page_data:
        page_data['properties']['status']['select']['name'] = new_status
        write_to_notion(page_id, page_data, auth_token)
    else:
        print('Page not found')