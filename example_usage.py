from client import NaturalLanguageFullstackWebAppArchitectClient

def main():
    client = NaturalLanguageFullstackWebAppArchitectClient()
    res = client.scaffold_production_app('Real-time crypto portfolio tracker with CoinGecko API and profit-loss chart')
    print('App Scaffold: ' + res['app_scaffold_id'] + ' | ' + res['app_name'])
    print('Components: ' + str(res['components_generated_count']) + ' | Type Safety: ' + str(res['typescript_type_safety_verified']))
    print('Live Preview: ' + res['live_instant_preview_url'])
    print('GitHub Repo: ' + res['github_sync_repo_url'])

if __name__ == '__main__':
    main()
