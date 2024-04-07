class ChainParent:
    """ChainParent class represents a component that has one or many chain components nested directly within it."""

    def __init__(self, allow_chain_deletion):
        self.__allow_chain_deletion = allow_chain_deletion
        self.__children = []

    def delete_chain_component(self, id: int):
        """
        Deletes a chain component from one of the child chains.

        Args:
             id (int): The id of the component to be deleted.
        """
        for child in self.__children:
            prev_component, to_delete = child.get_chain_component(id)
            if to_delete and prev_component:
                prev_component.set_next(to_delete.get_next())
                return
            if (
                to_delete
                and not to_delete.get_next()
                and not self.__allow_chain_deletion
            ):
                return
            if to_delete:
                self.__children = [
                    child for child in self.__children if child.get_internal_id() != id
                ]
                if to_delete.get_next():
                    self.__children.append(to_delete.get_next())
                return to_delete.get_next()

    def add_child(self, child):
        self.__children.append(child)

    def get_children(self):
        return self.__children
