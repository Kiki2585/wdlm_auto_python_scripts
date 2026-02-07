from auto_login_wldm import *

def auto_acryllic():
    click_with_certainty(r"..\resources\images\obj_large_assembly_tool.png")
    click_with_certainty(r"..\resources\images\button_use.png")
    click_with_certainty(r"..\resources\images\list_elevator.png")
    for _ in range(5):
        pya.scroll(-2000)
    time.sleep(1)
    click_with_certainty(r"..\resources\images\list_spacecraft.png")
    click_with_certainty(r"..\resources\images\component_tit_ball.png")
    click_with_certainty(r"..\resources\images\component_small_nuc_plant.png")
    click_with_certainty(r"..\resources\images\component_refridgerant.png")
    click_with_certainty(r"..\resources\images\component_water_pipe.png")
    click_with_certainty(r"..\resources\images\component_acryllic_plate.png")
    click_with_certainty(r"..\resources\images\button_ok.png")
    click_with_certainty(r"..\resources\images\button_producting.png")
    click_with_certainty(r"..\resources\images\button_start.png")
    click_with_certainty(r"..\resources\images\list_sam.png")
    time.sleep(4*60)

def auto_refridgerent():
    click_with_certainty(r"..\resources\images\obj_large_assembly_tool.png")
    click_with_certainty(r"..\resources\images\button_use.png")
    click_with_certainty(r"..\resources\images\list_elevator.png")
    for _ in range(5):
        pya.scroll(-2000)
    time.sleep(1)
    click_with_certainty(r"..\resources\images\list_spacecraft.png")
    click_with_certainty(r"..\resources\images\component_tit_ball.png")
    click_with_certainty(r"..\resources\images\component_small_nuc_plant.png")
    click_with_certainty(r"..\resources\images\component_refridgerant.png")

    click_with_certainty(r"..\resources\images\button_ok.png")
    click_with_certainty(r"..\resources\images\button_producting.png")
    click_with_certainty(r"..\resources\images\button_start.png")
    click_with_certainty(r"..\resources\images\list_sam.png")
    time.sleep(12*60)

def potion_diff_renew_timed(minutes, potion_pic):
    time.sleep(minutes*60)
    a = click_with_certainty(potion_pic)
    while a is not None:
        a = click_with_certainty(potion_pic)
    print("potion {%s} renewed.", potion_pic)

def auto_propeller():
    click_with_certainty(r"..\resources\images\obj_large_assembly_tool.png")
    click_with_certainty(r"..\resources\images\button_use.png")
    click_with_certainty(r"..\resources\images\list_elevator.png")
    for _ in range(5):
        pya.scroll(-2000)
    time.sleep(1)
    click_with_certainty(r"..\resources\images\list_spacecraft.png")
    click_with_certainty(r"..\resources\images\component_propeller.png")
    click_with_certainty(r"..\resources\images\button_ok.png")
    click_with_certainty(r"..\resources\images\button_producting.png")
    click_with_certainty(r"..\resources\images\button_start.png")
    click_with_certainty(r"..\resources\images\list_sam.png")
    time.sleep(12*60)

def auto_spacecraft():
    click_with_certainty(r"..\resources\images\obj_large_assembly_tool.png")
    click_with_certainty(r"..\resources\images\button_use.png")
    click_with_certainty(r"..\resources\images\list_elevator.png")
    for _ in range(5):
        pya.scroll(-2000)
    time.sleep(1)
    click_with_certainty(r"..\resources\images\list_spacecraft.png")
    click_with_certainty(r"..\resources\images\button_ok.png")
    click_with_certainty(r"..\resources\images\button_producting.png")
    click_with_certainty(r"..\resources\images\button_start.png")
    click_with_certainty(r"..\resources\images\list_sam.png")
    time.sleep(60*60)

def auto_france_church_bug():
    click_with_certainty(r"..\resources\images\button_other_accounts_loading.png")
    click_with_certainty(r"..\resources\images\button_login.png")
    if click_with_certainty(r"..\resources\images\button_enter_game.png") is not None:
        raise pya.ImageNotFoundException
    else:
        click_with_certainty(r"..\resources\images\button_confirm.png")
if __name__ == "__main__":
    time.sleep(10)
    ''' for _ in range(22):
        auto_acryllic()
        
    for _ in range(4):
        auto_refridgerent()
        
    potion_diff_renew_timed((3*60)+43, "item_potion_5.png")
    
    time.sleep(7*60)
    auto_propeller()
    auto_spacecraft()
     
    while True:
        auto_france_church_bug()
        '''
    time.sleep(102*60)
    for _ in range(3):
        click_with_certainty(r"..\resources\images\item_potion_2.png")
