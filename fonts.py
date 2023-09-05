from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, Color



fonts = {
            'display_results':  Font(name='Calibri',
                                size=12,
                                bold=False,
                                italic=False,
                                vertAlign=None,
                                underline='none',
                                strike=False,
                                color='003366FF'),

    'display_options_excel':    Font(name='Calibri',
                                size=12,
                                bold=False,
                                italic=False,
                                vertAlign=None,
                                underline='none',
                                strike=False,
                                color='00010101'),
}

alignments = {
            'display_results':  Alignment(horizontal='center',
                                vertical='center',
                                text_rotation=0,
                                wrap_text=True,
                                shrink_to_fit=False,
                                indent=0),

    'display_options_excel':    Alignment(horizontal='center',
                                vertical='bottom',
                                text_rotation=0,
                                wrap_text=True,
                                shrink_to_fit=False,
                                indent=0),
}