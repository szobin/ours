import json
from django.http import JsonResponse


def get_logs(log_text):
    return json.loads(log_text)


def get_users(logs):
    users = {}
    for item in logs:
        client_id = item.get("client_id")
        if client_id is None:
            continue
        ref = item.get("document.referer")
        loc = item.get("document.location")

        if client_id not in users:
            user = [
                ref.lower().find(".ours.com") >= 0,
                loc.lower().find("shop.com/checkout") >= 0]
        else:
            user = users[client_id]
            user = [
                user[0] or (ref.lower().find(".ours.com") >= 0),
                user[1] or (loc.lower().find("shop.com/checkout") >= 0),
                ]
        users.update({client_id: user})

    return users


def view_api_process_log(request):
    try:
        rq = json.loads(request.body.decode("utf-8"))
        log_text = rq.get("log_text")
        if log_text is None:
            raise Exception("wrong params")
        logs = get_logs(log_text)
        users = get_users(logs)
        resp = {"status": 0, "users": users}
    except Exception as exc:
        resp = {"status": -1, "error": repr(exc)}
    return JsonResponse(resp)

