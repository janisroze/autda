from suit.apps import DjangoSuitConfig

class MyDjangoSuitConfig(DjangoSuitConfig):
    verbose_name = 'Autda'
    admin_name = 'Autda'
    # menu_position = 'vertical'
    menu_position = 'horizontal'

    menu = (


        {
            'label': 'System',
            'models': (
                'auth.user',
                'auth.group',

            ),
            'permissions': 'auth.is_superuser'
        },
        {
            'label': 'CRM',
            'url': 'http://nra.lv',
            'permissions': 'auth.is_superuser'
        },

    )