# Add device parameters, such as Model, Device MAC, IOS, Version
def check(iface_dct):
    result = {}
    if 'model' in iface_dct:
        if 'C3560' in iface_dct['model']:
            result['model'] = [iface_dct['model'], '31.04.2021']
        if 'C3650' in iface_dct['model']:
            result['model'] = [iface_dct['model'], '31.04.2026']
        if 'C3750' in iface_dct['model']:
            result['model'] = [iface_dct['model'], '31.10.2026'] 
        if 'C6504' in iface_dct['model']:
            result['model'] = [iface_dct['model'], '30.04.2024']
        if 'C6506' in iface_dct['model']:
            result['model'] = [iface_dct['model'], '31.10.2025']      
        else:
            result['model'] = [iface_dct['model'], 'N/A']
    if 'mac' in iface_dct.keys():
        result['mac'] = iface_dct['mac']
    if 'os' in iface_dct.keys():
        result['os'] = iface_dct['os']
    if 'ios' in iface_dct.keys():
        result['ios'] = iface_dct['ios']
    if 'serial' in iface_dct.keys():
        result['serial'] = iface_dct['serial']
    if 'spanning-tree' in iface_dct.keys():
        result['spanning-tree'] = iface_dct['spanning-tree']
    return result

def spanning_tree(iface_dct):
    #default BAD value for spanning-tree map
    result_spanning_tree_cost = '100'
    if 'spanning-tree' in iface_dct.keys():
        result_spanning_tree_cost = iface_dct['spanning-tree']
    return result_spanning_tree_cost