async def autoname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"⌚️ {HM}||›  {DEFAULTUSER} ‹||"
        LOGS.info(name)
        try:
            await catub(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"