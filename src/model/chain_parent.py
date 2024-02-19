class ChainParent:
    """ChainParent class represents a component that has one or many chain components nested directly within it."""

    def __init__(self):
        self.__children = []

    def delete(self, id: int):
        """
        Deletes a chain component from one of the child chains.

        Args:
         - id (int): The id of the component to be deleted.
        """
        for child in self.__children:
            to_delete, prev_component = child.get_chain_component(id)
            if to_delete and prev_component:
                prev_component.set_next(to_delete.get_next())
                return
            if to_delete and not to_delete.get_next():
                return
            if to_delete:
                self.__children = [
                    child for child in self.__children if child.get_id() != id
                ]
                self.__children.append(to_delete.get_next())
        raise ValueError(f"Component with invalid ID deleted {id}")
