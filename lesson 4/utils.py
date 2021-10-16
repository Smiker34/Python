def currency_rates(code):
    import requests
    Response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    Response = Response.text
    if len(code) < 3:
        return "None"
    code = code.upper()
    code_ind = Response.find(code)
    if code_ind == -1:
        return "None"
    value_ind_s = Response.find("<Value>", code_ind)
    value_ind_f = Response.find("</Value>", code_ind)
    value = Response[value_ind_s+7:value_ind_f]
    return float(value.replace(",", "."))