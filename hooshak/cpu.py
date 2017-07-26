from graph_tool.all import *

from hooshak.modeling import HooshakEntityMixin, HooshakUserMixin


class CPU:
    def __init__(self, g: Graph):
        self.g = g

    # def calculate_smart_score(self, user: HooshakUserMixin, entity: HooshakEntityMixin):
    #     out = []
    #     from hooshak.context import hooshex
    #     for path in all_paths(
    #             g=self.g,
    #             source=hooshex.warehouse.get_user_v_by_uid(user.get_hooshak_uid()),
    #             target=hooshex.warehouse.get_entity_v_by_uid(entity.get_hooshak_uid()),
    #             # weights=hooshex.warehouse.eprop_value,
    #             cutoff=3
    #
    #     ):
    #         if len(path) == 4:
    #             out.append((
    #                            hooshex.warehouse.eprop_value[self.g.edge(path[0], path[1])] *
    #                            hooshex.warehouse.eprop_value[self.g.edge(path[1], path[2])] *
    #                            hooshex.warehouse.eprop_value[self.g.edge(path[2], path[3])]) ** (1. / 3.)
    #                        )
    #             # elif len(path) == 2:
    #             #     return None
    #             #
    #             #     e = self.g.edge(path[0], path[1])
    #             #     self.g.remove_edge(e)
    #             #
    #             #     out = self.calculate_smart_score(user=user, entity=entity)
    #             #
    #             #     self.g.add_edge(path[0], path[1])
    #             #
    #             #     # return out
    #             #     # out.append('shit')
    #
    #         return out

    def calculate_smart_score(self, user_uid, entity_uid):
        """

        

        :param user_uid:
        :param entity_uid:
        :return:
        """


        out = []
        from hooshak.context import hooshex
        for path in all_paths(
                g=self.g,
                source=hooshex.warehouse.get_user_v_by_uid(user_uid),
                target=hooshex.warehouse.get_entity_v_by_uid(entity_uid),
                # weights=hooshex.warehouse.eprop_value,
                cutoff=3

        ):
            if len(path) == 4:



                out.append(round((
                               hooshex.warehouse.g.properties[('e', 'value')][self.g.edge(path[0], path[1])] *
                               hooshex.warehouse.g.properties[('e', 'value')][self.g.edge(path[2], path[1])] *
                               hooshex.warehouse.g.properties[('e', 'value')][self.g.edge(path[2], path[3])]) ** (1. / 3.)
                                 ))
                # elif len(path) == 2:
                #     return None
                #
                #     e = self.g.edge(path[0], path[1])
                #     self.g.remove_edge(e)
                #
                #     out = self.calculate_smart_score(user=user, entity=entity)
                #
                #     self.g.add_edge(path[0], path[1])
                #
                #     # return out
                #     # out.append('shit')

        return out
