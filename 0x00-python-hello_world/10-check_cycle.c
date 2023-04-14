#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - check if list is a cycle
 * @list: pointer to list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL)
		return (0);

	hare = list;
	turtle = list;
	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;

		if (turtle == hare)
			return (1);
	}
	return (0);
}
