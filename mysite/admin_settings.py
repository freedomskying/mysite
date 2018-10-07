SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '五矿信托信息管理系统',
    'HEADER_DATE_FORMAT': 'l, j. F Y',  # Saturday, 16th March 2013
    'HEADER_TIME_FORMAT': 'H:i',  # 18:42

    # forms
    # Automatically adds asterisk symbol * to the end of every required field label:
    'SHOW_REQUIRED_ASTERISK': True,
    # Alert will be shown, when you’ll try to leave page, without saving changed form first
    'CONFIRM_UNSAVED_CHANGES': True,

    # menu
    # 'SEARCH_URL': 'admin:auth_user_changelist',
    # 'MENU_ICONS': {
    #     'sites': 'icon-leaf',
    #     'auth': 'icon-lock',
    # },
    # 'MENU': ({'label': '用户',
    #           'app': '用户',
    #           'models': ('UserProfile',)},
    #          ),
    'MENU': (

        # Keep original label and models
        'sites',

        # Rename app and set icon
        {'app': 'auth', 'label': 'Authorization', 'icon': 'icon-lock'},

        # Reorder app models
        {'app': 'auth', 'models': ('user', 'group')},

        # Custom app, with models
        {'label': 'Settings', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},

        # Cross-linked models with custom name; Hide default icon
        {'label': 'Custom', 'icon': None, 'models': (
            'auth.group',
            {'model': 'auth.user', 'label': 'Staff'}
        )},

        # Custom app, no models (child links)
        {'label': 'Users', 'url': 'auth.user', 'icon': 'icon-user'},

        # Separator
        '-',

        # Custom app and model with permissions
        {'label': 'Secure', 'permissions': 'auth.add_user', 'models': [
            {'label': 'custom-child', 'permissions': ('auth.add_user', 'auth.add_group')}
        ]},
    ),
    # 每一个字典表示左侧菜单的一栏
    # label表示name，app表示上边的install的app，models表示用了哪些models

    # misc
    'LIST_PER_PAGE': 20
}
