.. ALOC: A Logical Outline Creator documentation master file, created by
   sphinx-quickstart on Thu Mar 28 12:14:33 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ALOC: A Logical Outline Creator's Documentation
===========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. toctree::
   :maxdepth: 1
   :caption: Features
   :hidden:

   markdown/components
   markdown/the_aloc_spec

.. toctree::
   :maxdepth: 1
   :caption: Development
   :hidden:

   markdown/development



Getting Started
===============

Installation
------------

To install, first you'll need to clone this repository to your system using git:

.. code:: bash

   $ git clone git@github.com:sudoPom/aloc-final-year-project.git

Then enter the repository you just cloned and install all the requirements from the provided ``requirements.txt`` file.

.. code:: bash

   $ cd aloc-final-year-project
   $ pip install -r requirements.txt

You are then free to run ALOC as follows:

.. code:: bash

   $ python3 main.py


Your First Contract
-------------------

ALOC is a data-driven, visual editor designed for developing legal smart contracts in CoLa. CoLa is an English Controlled Natual Language (CNL) designed by Simon Fattal as part of their dissertation at UCL, you can read more about it `here <https://christopherclack.com/images/Documents/2021-SimonFattal-dissertation-MEng-distinction.pdf>`_.

You can draft documents by adding new "components" to the editor by pressing the "Contract" button:

Once a component is added, you can click on it to bring up editing options. To change the semantics of the component you can press the "Update" button. This will bring up a menu that will allow you to modify certain attributes of the component.

In order to conform to CoLa's grammar, certain attributes can only take certain values, but don't worry - ALOC will automatically tell you if a value you enter is not valid CoLa:

Once you have finished, press the submit button and you will be taken back to the main editor, with your changed component:

After you have added all your components you can save your contract by pressing the "Save Contract" button in the toolbar at the top of the editor. You can also export the contract to a ``.txt`` file by pressing the "Export Contract" button:

The exported file will then contain the **pure** CoLa of the contract you have drafted:

.. code:: bash

   $ cat contract.txt
   [0] ROSE IS RED
   C-AND
   [1] VIOLET IS BLUE
   C-AND
   [2] FLAG IS WIN
   C-AND
   [3] BABA IS YOU

This contract only makes use of "simple components" but base ALOC also has "conditional" and "chain" components, which you can read about :ref:`here <Components>`.

Customising ALOC
----------------

ALOC's power stems not from it's ability to draft contracts, but from the ability to customise the language it supports. This can be done through the use of ALOC specifications. Which you can read about :ref:`here <The ALOC Specification>`. Being able to create new ALOC specifications will allow you to quickly tinker ALOC to more specific languages - even for CNLs unrelated to law!


Extending ALOC
--------------

ALOC has plenty of room to grow, and if you'd like to help extend it please have a look at the :ref:`development section <Architecture>`. Additionally, you can make use of the code reference.

.. toctree::
   :maxdepth: 1
   :caption: Reference
   
   apidocs/contract
   apidocs/components
   apidocs/frame
   apidocs/specifications
   apidocs/aloc_specifications
   apidocs/terminals
