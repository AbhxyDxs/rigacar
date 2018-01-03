# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

import bpy

WIDGETS_LAYER = 19


def create():
    layers = [False] * 20
    layers[WIDGETS_LAYER] = True

    for name, widget in get_widgets().items():
        object_name = 'WGT-CarRig.%s' % name
        if object_name not in bpy.data.objects:
            m = bpy.data.meshes.new(object_name)
            m.from_pydata(widget['vertices'], widget['edges'], [])
            o = bpy.data.objects.new(object_name, m)
        else:
            o = bpy.data.objects[object_name]

        if object_name not in bpy.context.scene.objects:
            ob = bpy.context.scene.objects.link(o)
            ob.layers = layers


def get_widgets():
    widgets = {}
    widgets['Drift'] = {
        'vertices': [(0.560016930103302, 3.5614462490229926e-07, 0.0), (0.5472726821899414, 0.051212746649980545, 0.0),
                     (0.5173879265785217, 0.09973714500665665, 0.0), (0.4643173813819885, 0.14344893395900726, 0.0),
                     (0.3959912657737732, 0.1842898577451706, 0.0), (0.3111281096935272, 0.21670186519622803, 0.0),
                     (0.21430844068527222, 0.2407861351966858, 0.0), (0.10925304144620895, 0.2556171119213104, 0.0),
                     (0.5551204085350037, 0.025475479662418365, 0.0), (0.5348702073097229, 0.07644488662481308, 0.0),
                     (0.4915122985839844, 0.12226644158363342, 0.0), (0.4308139681816101, 0.1645427942276001, 0.0),
                     (0.3535597026348114, 0.2004958689212799, 0.0), (0.2627182900905609, 0.22874398529529572, 0.0),
                     (0.16178074479103088, 0.2482016384601593, 0.0), (0.05462652072310448, 0.2581210136413574, 0.0),
                     (0.4683051109313965, 2.978201791847823e-07, 0.0), (0.46016228199005127, 0.03240064159035683, 0.0),
                     (0.43346360325813293, 0.06059274449944496, 0.0), (0.38938117027282715, 0.08542850613594055, 0.0),
                     (0.33114129304885864, 0.110313281416893, 0.0), (0.2601758539676666, 0.13103415071964264, 0.0),
                     (0.17921197414398193, 0.1465274840593338, 0.0), (0.09136109799146652, 0.15609556436538696, 0.0),
                     (0.4649912118911743, 0.015658844262361526, 0.0), (0.450432151556015, 0.04798557236790657, 0.0),
                     (0.41178521513938904, 0.07347165793180466, 0.0), (0.3602612316608429, 0.09748400002717972, 0.0),
                     (0.29565858840942383, 0.12036669254302979, 0.0), (0.21969391405582428, 0.13851231336593628, 0.0),
                     (0.13528653979301453, 0.15106302499771118, 0.0), (0.04568054899573326, 0.15747304260730743, 0.0),
                     (-0.560016930103302, 3.5614462490229926e-07, 0.0), (-0.5472726821899414, 0.051212746649980545, 0.0),
                     (-0.5173879265785217, 0.09973714500665665, 0.0), (-0.46497008204460144, 0.14364132285118103, 0.0),
                     (-0.3959912657737732, 0.1842898577451706, 0.0), (-0.3111281096935272, 0.21670186519622803, 0.0),
                     (-0.21430844068527222, 0.2407861351966858, 0.0), (-0.10925304144620895, 0.2556171119213104, 0.0),
                     (-0.5551204085350037, 0.025475479662418365, 0.0), (-0.5348702073097229, 0.07644488662481308, 0.0),
                     (-0.4915122985839844, 0.12226644158363342, 0.0), (-0.4308139681816101, 0.1645427942276001, 0.0),
                     (-0.3535597026348114, 0.2004958689212799, 0.0), (-0.2627182900905609, 0.22874398529529572, 0.0),
                     (-0.16178074479103088, 0.2482016384601593, 0.0), (-0.05462652072310448, 0.2581210136413574, 0.0),
                     (-0.4683051109313965, 2.978201791847823e-07, 0.0), (-0.46016228199005127, 0.03240064159035683, 0.0),
                     (-0.43346360325813293, 0.06059274449944496, 0.0), (-0.38938117027282715, 0.08542850613594055, 0.0),
                     (-0.33114129304885864, 0.110313281416893, 0.0), (-0.2601758539676666, 0.13103415071964264, 0.0),
                     (-0.17921197414398193, 0.1465274840593338, 0.0), (-0.09136109799146652, 0.15609556436538696, 0.0),
                     (-0.4649912118911743, 0.015658844262361526, 0.0), (-0.450432151556015, 0.04798557236790657, 0.0),
                     (-0.41178521513938904, 0.07347165793180466, 0.0), (-0.3602612316608429, 0.09748400002717972, 0.0),
                     (-0.29565858840942383, 0.12036669254302979, 0.0), (-0.21969391405582428, 0.13851231336593628, 0.0),
                     (-0.13528653979301453, 0.15106302499771118, 0.0), (-0.04568054899573326, 0.15747304260730743, 0.0),
                     (0.0, 0.26062488555908203, 0.0), (0.0, 0.15932999551296234, 0.0)],
        'edges': [(8, 0), (9, 1), (10, 2), (11, 3), (12, 4), (13, 5), (14, 6), (15, 7), (1, 8), (2, 9), (3, 10), (4, 11),
                  (5, 12), (6, 13), (7, 14), (64, 15), (24, 16), (25, 17), (26, 18), (27, 19), (28, 20), (29, 21),
                  (30, 22), (31, 23), (17, 24), (18, 25), (19, 26), (20, 27), (21, 28), (22, 29), (23, 30), (65, 31),
                  (0, 16), (24, 8), (1, 17), (25, 9), (40, 32), (41, 33), (42, 34), (43, 35), (44, 36), (45, 37), (46, 38),
                  (47, 39), (33, 40), (34, 41), (35, 42), (36, 43), (37, 44), (38, 45), (39, 46), (64, 47), (56, 48),
                  (57, 49), (58, 50), (59, 51), (60, 52), (61, 53), (62, 54), (63, 55), (49, 56), (50, 57), (51, 58),
                  (52, 59), (53, 60), (54, 61), (55, 62), (65, 63), (32, 48), (56, 40), (33, 49), (57, 41)]
    }

    widgets['Root'] = {
        'vertices': [(-0.5, -0.8844379782676697, 0.0), (-0.3844379782676697, -1.0, 0.0), (-0.4912033677101135, -0.9286617040634155, 0.0),
                     (-0.4661526679992676, -0.9661527276039124, 0.0), (-0.42866164445877075, -0.9912034273147583, 0.0), (0.3844379782676697, -1.0, 0.0),
                     (0.5, -0.8844379782676697, 0.0), (0.42866164445877075, -0.9912034273147583, 0.0), (0.4661526679992676, -0.9661527276039124, 0.0),
                     (0.4912033677101135, -0.9286617040634155, 0.0), (-0.5, 0.8844379782676697, 0.0), (-0.3844379782676697, 1.0, 0.0),
                     (-0.4912033677101135, 0.9286617040634155, 0.0), (-0.4661526679992676, 0.9661527276039124, 0.0), (-0.42866164445877075, 0.9912034273147583, 0.0),
                     (0.5, 0.8844379782676697, 0.0), (0.3844379782676697, 1.0, 0.0), (0.4912033677101135, 0.9286617040634155, 0.0),
                     (0.4661526679992676, 0.9661527276039124, 0.0), (0.42866164445877075, 0.9912034273147583, 0.0), (0.1234154999256134, -1.0, 0.0),
                     (-0.1234154999256134, -1.0, 0.0), (0.1234154999256134, -1.0971899032592773, 0.0), (-0.1234154999256134, -1.0971899032592773, 0.0),
                     (0.3031257688999176, -1.0971899032592773, 0.0), (-0.3031257688999176, -1.0971899032592773, 0.0), (0.0, -1.25, 0.0)],
        'edges': [(0, 2), (2, 3), (3, 4), (4, 1), (5, 7), (7, 8), (8, 9), (9, 6), (10, 12), (12, 13), (13, 14), (14, 11), (15, 17), (17, 18), (18, 19),
                  (19, 16), (0, 10), (6, 15), (11, 16), (20, 5), (21, 1), (22, 20), (23, 21), (24, 22), (25, 23), (26, 24), (26, 25)]
    }

    widgets['GroundSensor'] = {
        'vertices': [(-0.5, -0.822191596031189, 0.0), (-0.32219159603118896, -1.0, 0.0), (-0.4761781692504883, -0.9110957980155945, 0.0),
                     (-0.4110957980155945, -0.9761781692504883, 0.0), (0.32219159603118896, -1.0, 0.0), (0.5, -0.822191596031189, 0.0),
                     (0.4110957980155945, -0.9761781692504883, 0.0), (0.47617819905281067, -0.9110957980155945, 0.0), (-0.5, 0.822191596031189, 0.0),
                     (-0.32219159603118896, 1.0, 0.0), (-0.4761781692504883, 0.9110957980155945, 0.0), (-0.4110957980155945, 0.9761781692504883, 0.0),
                     (0.5, 0.822191596031189, 0.0), (0.32219159603118896, 1.0, 0.0), (0.4761781692504883, 0.9110957980155945, 0.0),
                     (0.4110957980155945, 0.9761781692504883, 0.0)],
        'edges': [(0, 2), (2, 3), (3, 1), (4, 6), (6, 7), (7, 5), (8, 10), (10, 11), (11, 9), (12, 14), (14, 15), (15, 13), (0, 8), (1, 4), (5, 12), (9, 13)]
    }

    widgets['Wheel'] = {
        'vertices': [(-1.1874363536890087e-07, 0.9999999403953552, -1.1874362826347351e-07), (-1.043081283569336e-07, 0.9807851910591125, 0.19509020447731018),
                     (-8.940696716308594e-08, 0.9238794445991516, 0.38268333673477173), (-1.1920928955078125e-07, 0.8314695358276367, 0.555570125579834),
                     (-5.960464477539063e-08, 0.7071067094802856, 0.7071066498756409), (-5.960464477539063e-08, 0.555570125579834, 0.8314695358276367),
                     (-5.960464477539063e-08, 0.3826833963394165, 0.9238793849945068), (-5.960464477539063e-08, 0.19509033858776093, 0.9807851314544678),
                     (-5.960464477539063e-08, 7.549790836947068e-08, 0.9999998807907104), (-5.960464477539063e-08, -0.195090189576149, 0.9807851910591125),
                     (-5.960464477539063e-08, -0.38268324732780457, 0.9238794445991516), (-5.960464477539063e-08, -0.555570125579834, 0.8314695358276367),
                     (-5.960464477539063e-08, -0.7071067094802856, 0.7071066498756409), (-1.1920928955078125e-07, -0.8314695954322815, 0.5555700659751892),
                     (-8.940696716308594e-08, -0.9238795638084412, 0.3826831579208374), (-1.043081283569336e-07, -0.9807852506637573, 0.19508996605873108),
                     (-1.1874365668518294e-07, -0.9999998211860657, -4.445849981493666e-07), (-1.341104507446289e-07, -0.9807851314544678, -0.19509084522724152),
                     (-1.4901161193847656e-07, -0.9238792657852173, -0.38268399238586426), (-1.1920928955078125e-07, -0.8314692378044128, -0.5555708408355713),
                     (-1.7881393432617188e-07, -0.7071062922477722, -0.7071073651313782), (-1.7881393432617188e-07, -0.555569589138031, -0.8314701318740845),
                     (-1.7881393432617188e-07, -0.3826826512813568, -0.9238799810409546), (-1.7881393432617188e-07, -0.1950894445180893, -0.9807855486869812),
                     (-1.1920928955078125e-07, 9.655991561885457e-07, -1.0000001192092896), (-1.7881393432617188e-07, 0.1950913369655609, -0.9807851910591125),
                     (-1.7881393432617188e-07, 0.3826844394207001, -0.9238792061805725), (-1.7881393432617188e-07, 0.5555711984634399, -0.8314690589904785),
                     (-1.7881393432617188e-07, 0.7071076035499573, -0.7071059942245483), (-1.1920928955078125e-07, 0.8314703106880188, -0.5555692315101624),
                     (-1.4901161193847656e-07, 0.9238800406455994, -0.382682204246521), (-1.341104507446289e-07, 0.9807854890823364, -0.1950889378786087),
                     (-1.1866376325997408e-07, 0.9439931511878967, -1.099180622077256e-07), (-1.0503674019446407e-07, 0.9258545637130737, 0.18416382372379303),
                     (-9.097014697090344e-08, 0.8721359372138977, 0.36125046014785767), (-1.191033334180247e-07, 0.7849016189575195, 0.5244544148445129),
                     (-6.283696052378218e-08, 0.6675039529800415, 0.667503833770752), (-6.283696052378218e-08, 0.5244544148445129, 0.7849015593528748),
                     (-6.283696052378218e-08, 0.36125051975250244, 0.8721358180046082), (-6.283696052378218e-08, 0.18416395783424377, 0.9258544445037842),
                     (-6.283696052378218e-08, 8.652769167838414e-08, 0.9439930319786072), (-6.283696052378218e-08, -0.18416379392147064, 0.925854504108429),
                     (-6.283696052378218e-08, -0.3612503409385681, 0.8721358776092529), (-6.283696052378218e-08, -0.5244543552398682, 0.7849015593528748),
                     (-6.283696052378218e-08, -0.6675038933753967, 0.667503833770752), (-1.191033334180247e-07, -0.7849015593528748, 0.5244543552398682),
                     (-9.097014697090344e-08, -0.8721359372138977, 0.36125028133392334), (-1.0503674019446407e-07, -0.9258545637130737, 0.18416360020637512),
                     (-1.1866378457625615e-07, -0.9439929723739624, -4.1751010826374113e-07), (-1.331699337470127e-07, -0.9258544445037842, -0.18416441977024078),
                     (-1.4723653407600068e-07, -0.8721356987953186, -0.3612510859966278), (-1.191033334180247e-07, -0.7849012613296509, -0.5244550704956055),
                     (-1.7536972052312194e-07, -0.6675034761428833, -0.6675045490264893), (-1.7536972052312194e-07, -0.52445387840271, -0.7849021553993225),
                     (-1.7536972052312194e-07, -0.36124980449676514, -0.8721364140510559), (-1.7536972052312194e-07, -0.18416307866573334, -0.9258548617362976),
                     (-1.191033334180247e-07, 9.267772043131117e-07, -0.9439932703971863), (-1.7536972052312194e-07, 0.18416491150856018, -0.925854504108429),
                     (-1.7536972052312194e-07, 0.36125150322914124, -0.8721356987953186), (-1.7536972052312194e-07, 0.5244554281234741, -0.7849010825157166),
                     (-1.7536972052312194e-07, 0.6675047874450684, -0.6675032377243042), (-1.191033334180247e-07, 0.7849022746086121, -0.5244535803794861),
                     (-1.4723653407600068e-07, 0.8721364140510559, -0.3612493872642517), (-1.331699337470127e-07, 0.9258548021316528, -0.18416263163089752)],
        'edges': [(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9), (11, 10), (12, 11), (13, 12), (14, 13), (15, 14), (16, 15),
                  (17, 16), (18, 17), (19, 18), (20, 19), (21, 20), (22, 21), (23, 22), (24, 23), (25, 24), (26, 25), (27, 26), (28, 27), (29, 28), (30, 29),
                  (31, 30), (0, 31), (33, 32), (34, 33), (35, 34), (36, 35), (37, 36), (38, 37), (39, 38), (40, 39), (41, 40), (42, 41), (43, 42), (44, 43),
                  (45, 44), (46, 45), (47, 46), (48, 47), (49, 48), (50, 49), (51, 50), (52, 51), (53, 52), (54, 53), (55, 54), (56, 55), (57, 56), (58, 57),
                  (59, 58), (60, 59), (61, 60), (62, 61), (63, 62), (32, 63)]
    }

    widgets['Steering'] = {
        'vertices': [(0.7296777367591858, 0.07034172862768173, 0.0), (0.057004380971193314, -0.07034172862768173, 0.0), (0.7296777367591858, -0.07034172862768173, 0.0),
                     (0.057004380971193314, 0.07034172862768173, 0.0), (0.7296777367591858, 0.16664999723434448, 0.0), (0.7296777367591858, -0.16664999723434448, 0.0),
                     (0.9998999834060669, 0.0, 0.0), (-0.7296777367591858, 0.07034172862768173, 0.0), (-0.057004380971193314, -0.07034172862768173, 0.0),
                     (-0.7296777367591858, -0.07034172862768173, 0.0), (-0.057004380971193314, 0.07034172862768173, 0.0), (-0.7296777367591858, 0.16664999723434448, 0.0),
                     (-0.7296777367591858, -0.16664999723434448, 0.0), (-0.9998999834060669, 0.0, 0.0)],
        'edges': [(2, 1), (3, 0), (1, 3), (0, 4), (5, 2), (4, 6), (6, 5), (9, 8), (10, 7), (8, 10), (7, 11), (12, 9), (11, 13), (13, 12)]
    }

    widgets['Suspension'] = {
        'vertices': [(-0.42728525400161743, -0.12928833067417145, 0.11859216541051865), (-0.06909304857254028, 0.2578587830066681, 0.16264206171035767),
                     (-0.13347753882408142, 0.23118986189365387, 0.16264206171035767), (-0.1887657195329666, 0.1887657195329666, 0.16264206171035767),
                     (-0.23118992149829865, 0.13347753882408142, 0.16264206171035767), (-0.2578587830066681, 0.06909307092428207, 0.16264206171035767),
                     (-0.42728525400161743, -0.06909316033124924, 0.1368037909269333), (-0.2578587830066681, -0.06909302622079849, 0.16264206171035767),
                     (-0.23118986189365387, -0.13347747921943665, 0.16264206171035767), (-0.18876579403877258, -0.18876568973064423, 0.16264206171035767),
                     (-0.1334775984287262, -0.23118983209133148, 0.16264206171035767), (-0.06909313797950745, -0.2578587532043457, 0.16264206171035767),
                     (-0.42728525400161743, 0.06909292191267014, 0.1368037909269333), (0.06909293681383133, -0.2578587830066681, 0.16264206171035767),
                     (0.13347743451595306, -0.23118995130062103, 0.16264206171035767), (0.18876565992832184, -0.18876583874225616, 0.16264206171035767),
                     (0.23118983209133148, -0.1334775984287262, 0.16264206171035767), (0.2578587532043457, -0.06909316033124924, 0.16264206171035767),
                     (0.42728525400161743, -0.06909316033124924, 0.1368037909269333), (0.2578587830066681, 0.06909292191267014, 0.16264206171035767),
                     (0.23118992149829865, 0.13347740471363068, 0.16264206171035767), (0.18876585364341736, 0.18876561522483826, 0.16264206171035767),
                     (0.13347768783569336, 0.2311897873878479, 0.16264206171035767), (0.0690932497382164, 0.2578587532043457, 0.16264206171035767),
                     (0.42728525400161743, 0.06909292191267014, 0.1368037909269333), (0.42728525400161743, -0.12928833067417145, 0.11859216541051865),
                     (0.42728525400161743, 0.12928791344165802, 0.11859223246574402), (0.6011841893196106, -2.227646831443053e-07, 0.04259913042187691),
                     (-0.42728525400161743, 0.12928791344165802, 0.11859223246574402), (-0.6011841893196106, -2.227646831443053e-07, 0.04259913042187691),
                     (-0.06909316033124924, -0.42728525400161743, 0.1368037909269333), (0.06909292191267014, -0.42728525400161743, 0.1368037909269333),
                     (-0.12928833067417145, -0.42728525400161743, 0.11859216541051865), (0.12928785383701324, -0.42728525400161743, 0.11859225481748581),
                     (-2.545882011872891e-07, -0.6011841893196106, 0.042599156498909), (-0.06909316033124924, 0.42728525400161743, 0.1368037909269333),
                     (0.06909292191267014, 0.42728525400161743, 0.1368037909269333), (-0.12928833067417145, 0.42728525400161743, 0.11859216541051865),
                     (0.12928785383701324, 0.42728525400161743, 0.11859223246574402), (-2.545882011872891e-07, 0.6011841893196106, 0.04259913042187691),
                     (0.0, 0.1595769226551056, 0.16264206171035767), (-0.0797884613275528, 0.13819767534732819, 0.16264206171035767),
                     (-0.13819767534732819, 0.079788438975811, 0.16264206171035767), (-0.1595769226551056, -6.975329203129377e-09, 0.16264206171035767),
                     (-0.13819767534732819, -0.0797884613275528, 0.16264206171035767), (-0.0797884613275528, -0.13819767534732819, 0.16264206171035767),
                     (-2.409544741510672e-08, -0.1595769226551056, 0.16264206171035767), (0.07978841662406921, -0.13819767534732819, 0.16264206171035767),
                     (0.1381976306438446, -0.07978851348161697, 0.16264206171035767), (0.1595769226551056, -7.418926628588451e-08, 0.16264206171035767),
                     (0.13819773495197296, 0.07978837937116623, 0.16264206171035767), (0.07978855073451996, 0.1381976157426834, 0.16264206171035767),
                     (0.3002154231071472, 0.06909292191267014, 0.16078221797943115), (0.34257203340530396, 0.06909292191267014, 0.15552930533885956),
                     (0.3849286139011383, 0.06909292191267014, 0.1473732590675354), (0.3849286139011383, -0.06909316033124924, 0.14737321436405182),
                     (0.34257200360298157, -0.06909316033124924, 0.15552933514118195), (0.30021539330482483, -0.06909316033124924, 0.16078221797943115),
                     (-0.3002154231071472, 0.06909303367137909, 0.16078221797943115), (-0.34257203340530396, 0.0690929964184761, 0.15552930533885956),
                     (-0.3849286139011383, 0.06909295171499252, 0.1473732590675354), (-0.3849286139011383, -0.06909313052892685, 0.1473732590675354),
                     (-0.34257200360298157, -0.06909309327602386, 0.15552935004234314), (-0.30021539330482483, -0.06909305602312088, 0.16078220307826996),
                     (-0.06909314543008804, -0.30021539330482483, 0.16078221797943115), (-0.06909314543008804, -0.34257200360298157, 0.15552933514118195),
                     (-0.06909315288066864, -0.3849286139011383, 0.14737321436405182), (0.06909293681383133, -0.3002154231071472, 0.16078221797943115),
                     (0.06909292936325073, -0.34257203340530396, 0.15552930533885956), (0.06909292191267014, -0.3849286139011383, 0.1473732590675354),
                     (-0.06909307837486267, 0.3002154231071472, 0.16078221797943115), (-0.06909310817718506, 0.34257203340530396, 0.15552930533885956),
                     (-0.06909313052892685, 0.3849286139011383, 0.1473732590675354), (0.06909316033124924, 0.30021539330482483, 0.16078221797943115),
                     (0.06909307837486267, 0.34257200360298157, 0.15552933514118195), (0.0690930038690567, 0.3849286139011383, 0.14737321436405182)],
        'edges': [(2, 1), (3, 2), (4, 3), (5, 4), (12, 28), (0, 6), (8, 7), (9, 8), (10, 9), (11, 10), (28, 29), (29, 0), (14, 13), (15, 14), (16, 15), (17, 16),
                  (54, 24), (57, 17), (20, 19), (21, 20), (22, 21), (23, 22), (60, 12), (25, 18), (24, 26), (27, 25), (26, 27), (63, 7), (32, 30), (31, 33),
                  (34, 32), (33, 34), (66, 30), (69, 31), (37, 35), (36, 38), (39, 37), (38, 39), (72, 35), (75, 36), (41, 40), (42, 41), (43, 42), (44, 43),
                  (45, 44), (46, 45), (47, 46), (48, 47), (49, 48), (50, 49), (51, 50), (40, 51), (19, 52), (52, 53), (53, 54), (18, 55), (55, 56), (56, 57),
                  (5, 58), (58, 59), (59, 60), (6, 61), (61, 62), (62, 63), (11, 64), (64, 65), (65, 66), (13, 67), (67, 68), (68, 69), (1, 70), (70, 71),
                  (71, 72), (23, 73), (73, 74), (74, 75)]
    }

    widgets['WheelDamper'] = {
        'vertices': [(-0.17770397663116455, -0.09192684292793274, 0.14030149579048157), (-0.17770397663116455, -0.09192684292793274, 0.23383590579032898),
                     (-0.10793274641036987, -0.16846297681331635, 0.13250692188739777), (-0.10793278366327286, -0.16846297681331635, 0.22604137659072876),
                     (-0.009241040796041489, -0.1998595893383026, 0.12471239268779755), (-0.009241056628525257, -0.19985966384410858, 0.21824686229228973),
                     (0.09192679077386856, -0.17770402133464813, 0.11691785603761673), (0.09192682057619095, -0.17770402133464813, 0.21045231819152832),
                     (0.16846293210983276, -0.10793281346559525, 0.1091233491897583), (0.16846293210983276, -0.10793281346559525, 0.2026577889919281),
                     (0.1998595893383026, -0.009241072461009026, 0.10132881999015808), (0.1998595893383026, -0.009241089224815369, 0.19486328959465027),
                     (0.17770397663116455, 0.09192679077386856, 0.09353431314229965), (0.1777040809392929, 0.09192677587270737, 0.18706879019737244),
                     (0.10793274641036987, 0.16846294701099396, 0.08573977649211884), (0.10793281346559525, 0.16846294701099396, 0.17927424609661102),
                     (0.009240993298590183, 0.19985954463481903, 0.0779452696442604), (0.009241056628525257, 0.1998595893383026, 0.1714797168970108),
                     (-0.09192684292793274, 0.17770391702651978, 0.07015073299407959), (-0.09192682057619095, 0.17770402133464813, 0.16368518769741058),
                     (-0.16846294701099396, 0.10793264955282211, 0.06235618144273758), (-0.16846297681331635, 0.10793274641036987, 0.15589064359664917),
                     (-0.19985954463481903, 0.009240960702300072, 0.05456162989139557), (-0.1998595893383026, 0.00924102496355772, 0.14809606969356537),
                     (-0.17770391702651978, -0.09192687273025513, 0.04676707834005356), (-0.17770402133464813, -0.09192684292793274, 0.14030154049396515),
                     (-0.1079326793551445, -0.16846294701099396, 0.03897252678871155), (-0.10793278366327286, -0.16846302151679993, 0.13250696659088135),
                     (-0.00924097653478384, -0.19985954463481903, 0.03117799013853073), (-0.009241056628525257, -0.19985966384410858, 0.12471242249011993),
                     (0.09192684292793274, -0.17770391702651978, 0.02338346280157566), (0.09192682057619095, -0.1777040809392929, 0.11691789329051971),
                     (0.16846293210983276, -0.1079326942563057, 0.015588936395943165), (0.16846293210983276, -0.10793283581733704, 0.10912337899208069),
                     (0.19985954463481903, -0.009240993298590183, 0.0077944230288267136), (0.1998595893383026, -0.009241105057299137, 0.10132886469364166),
                     (0.17770391702651978, 0.09192683547735214, -9.42906623890849e-08), (0.1777040809392929, 0.09192677587270737, 0.09353433549404144),
                     (0.1079326793551445, 0.16846290230751038, -0.007794610224664211), (0.10793281346559525, 0.16846294701099396, 0.08573982864618301),
                     (0.00924097653478384, 0.19985945522785187, -0.015589137561619282), (0.009241056628525257, 0.1998595893383026, 0.0779452919960022),
                     (-0.09192682057619095, 0.177703857421875, -0.023383673280477524), (-0.09192682057619095, 0.17770402133464813, 0.07015074789524078),
                     (-0.16846290230751038, 0.10793262720108032, -0.031178224831819534), (-0.16846294701099396, 0.10793274641036987, 0.06235621124505997),
                     (-0.19985945522785187, 0.009240944869816303, -0.03897276148200035), (-0.1998595893383026, 0.00924102496355772, 0.05456166714429855),
                     (-0.177703857421875, -0.09192684292793274, -0.046767283231019974), (-0.17770402133464813, -0.09192684292793274, 0.04676711559295654),
                     (-0.10793262720108032, -0.16846290230751038, -0.054561812430620193), (-0.10793278366327286, -0.16846302151679993, 0.038972560316324234),
                     (-0.009240960702300072, -0.19985948503017426, -0.062356337904930115), (-0.00924102496355772, -0.19985966384410858, 0.031178021803498268),
                     (0.09192684292793274, -0.177703857421875, -0.07015086710453033), (0.09192683547735214, -0.17770402133464813, 0.023383498191833496),
                     (0.16846293210983276, -0.10793262720108032, -0.07794538885354996), (0.16846302151679993, -0.10793278366327286, 0.015588970854878426),
                     (0.19985945522785187, -0.009240944869816303, -0.08573991060256958), (0.19985966384410858, -0.009241040796041489, 0.007794454228132963),
                     (0.1777038276195526, 0.09192683547735214, -0.09353446215391159), (0.1777040809392929, 0.09192684292793274, -6.286042264491698e-08),
                     (0.10793259739875793, 0.1684628427028656, -0.10132896900177002), (0.10793281346559525, 0.16846302151679993, -0.007794579025357962),
                     (0.00924092996865511, 0.1998593956232071, -0.10912348330020905), (0.009241040796041489, 0.19985966384410858, -0.015589105896651745),
                     (-0.09192682057619095, 0.17770376801490784, -0.11691801995038986), (-0.09192684292793274, 0.17770405113697052, -0.023383641615509987),
                     (-0.1684628427028656, 0.10793255269527435, -0.12471257150173187), (-0.16846302151679993, 0.10793274641036987, -0.031178191304206848),
                     (-0.1998593509197235, 0.009240913204848766, -0.1325071007013321), (-0.19985966384410858, 0.009240993298590183, -0.03897274285554886),
                     (-0.17770376801490784, -0.09192683547735214, -0.1403016299009323), (-0.17770402133464813, -0.09192688763141632, -0.046767283231019974),
                     (-0.10793255269527435, -0.1684628427028656, -0.14809612929821014), (-0.10793274641036987, -0.16846303641796112, -0.054561812430620193),
                     (-0.009240896441042423, -0.1998593509197235, -0.15589067339897156), (-0.009240993298590183, -0.19985966384410858, -0.062356337904930115),
                     (0.09192683547735214, -0.17770375311374664, -0.16368518769741058), (0.09192688763141632, -0.17770402133464813, -0.07015086710453033),
                     (0.1684628129005432, -0.10793253034353256, -0.1714797168970108), (0.16846302151679993, -0.10793274641036987, -0.07794538885354996),
                     (0.1998593509197235, -0.009240913204848766, -0.17927424609661102), (0.1998595893383026, -0.009241009131073952, -0.08573991060256958),
                     (0.17770375311374664, 0.09192679077386856, -0.18706879019737244), (0.17770397663116455, 0.09192684292793274, -0.09353446215391159),
                     (0.10793255269527435, 0.1684628278017044, -0.19486330449581146), (0.10793274641036987, 0.16846294701099396, -0.10132896900177002),
                     (0.00924092996865511, 0.1998593509197235, -0.20265783369541168), (0.00924102496355772, 0.19985954463481903, -0.10912348330020905),
                     (-0.09192678332328796, 0.17770370841026306, -0.2104523628950119), (-0.09192679077386856, 0.17770394682884216, -0.11691801995038986),
                     (-0.1684628129005432, 0.10793255269527435, -0.21824689209461212), (-0.16846290230751038, 0.10793272405862808, -0.12471257150173187),
                     (-0.19985929131507874, 0.00924092996865511, -0.22604137659072876), (-0.19985954463481903, 0.00924102496355772, -0.1325071007013321),
                     (-0.17770370841026306, -0.09192678332328796, -0.23383590579032898), (-0.17770391702651978, -0.09192680567502975, -0.1403016299009323),
                     (-0.21371114253997803, -0.21371114253997803, 0.24772925674915314), (0.21371114253997803, -0.21371114253997803, 0.24772925674915314),
                     (-0.21371114253997803, 0.21371114253997803, 0.24772925674915314), (0.21371114253997803, 0.21371114253997803, 0.24772925674915314),
                     (-0.21371114253997803, -0.21371114253997803, -0.24772925674915314), (0.21371114253997803, -0.21371114253997803, -0.24772925674915314),
                     (-0.21371114253997803, 0.21371114253997803, -0.24772925674915314), (0.21371114253997803, 0.21371114253997803, -0.24772925674915314)],
        'edges': [(1, 3), (2, 0), (3, 5), (4, 2), (5, 7), (6, 4), (7, 9), (8, 6), (9, 11), (10, 8), (11, 13), (12, 10), (13, 15), (14, 12),
                  (15, 17), (16, 14), (17, 19), (18, 16), (19, 21), (20, 18), (21, 23), (22, 20), (23, 25), (24, 22), (25, 27), (26, 24),
                  (27, 29), (28, 26), (29, 31), (30, 28), (31, 33), (32, 30), (33, 35), (34, 32), (35, 37), (36, 34), (37, 39), (38, 36),
                  (39, 41), (40, 38), (41, 43), (42, 40), (43, 45), (44, 42), (45, 47), (46, 44), (47, 49), (48, 46), (49, 51), (50, 48),
                  (51, 53), (52, 50), (53, 55), (54, 52), (55, 57), (56, 54), (57, 59), (58, 56), (59, 61), (60, 58), (61, 63), (62, 60),
                  (63, 65), (64, 62), (65, 67), (66, 64), (67, 69), (68, 66), (69, 71), (70, 68), (71, 73), (72, 70), (73, 75), (74, 72),
                  (75, 77), (76, 74), (77, 79), (78, 76), (79, 81), (80, 78), (81, 83), (82, 80), (83, 85), (84, 82), (85, 87), (86, 84),
                  (87, 89), (88, 86), (89, 91), (90, 88), (91, 93), (92, 90), (93, 95), (94, 92), (95, 97), (96, 94), (100, 98), (98, 99),
                  (99, 101), (101, 100), (104, 102), (102, 103), (103, 105), (105, 104)]
    }

    return widgets

if __name__ == "__main__":
    create()
