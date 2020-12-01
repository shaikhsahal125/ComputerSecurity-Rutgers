echo AddUser test - these should pass
for n in `seq -f '%02.0f' 5`; do $cmd AddUser user-$n pass-$n ;
done

echo Authenticate test - these should pass
# test authenticate - should pass
for n in `seq -f '%02.0f' 5`; do $cmd Authenticate user-$n pass-$n ;
done

echo AddUser test - these should fail
# test add duplicate users - should fail
for n in `seq -f '%02.0f' 5`; do
	$cmd AddUser user-$n pass-${n}-diff ;
done

echo Authenticate test bad passwords - these should fail
# test authenticate with bad passwords - should fail
for n in `seq -f '%02.0f' 5`; do
	$cmd Authenticate user-$n pass-${n}-bad ;
done

echo Authenticate test bad user names - these should fail
# test authenticate with bad user names - should fail
for n in `seq -f '%02.0f' 5`; do
	$cmd Authenticate user-${n}-bad pass-$n ;
done

# test bad user or empty password - both should fail
echo Authenticate test empty user name - should fail
$cmd Authenticate "" password
echo Authenticate test empty password - should fail
$cmd Authenticate user ""

read -p "check finished?" ck

# add users to a few domains

echo SetDomain test - should pass
for n in `seq -f '%02.0f' 4`; do
	$cmd SetDomain user-$n domain-1 ;
done

for n in `seq -f '%02.0f' 5`; do
	$cmd SetDomain user-$n domain-2 ;
done

for n in `seq -f '%02.0f' 5`; do
	$cmd SetDomain user-$n domain-$n ;
done

# list users in the domain
echo DomainInfo test - should pass
$cmd DomainInfo domain-1 # should show user-01 .. user-04
$cmd DomainInfo domain-2 # should show user-01 .. user-05

echo DomainInfo test - should fail
$cmd DomainInfo domain-bad # should fail

# add a bad user - should fail
echo SetDomain test - should fail
$cmd SetDomain bad-name domain-1

read -p "check finished?" ck
# add objects to a few types

echo SetType test - should pass
for n in `seq -f '%02.0f' 4`; do
	$cmd SetType object-$n type-1 ;
done
for n in `seq -f '%02.0f' 5`; do
	$cmd SetType object-$n type-2 ;
done
for n in `seq -f '%02.0f' 5`; do
	$cmd SetType object-$n type-$n ;
done

# list objects in the type
echo TypeInfo test - should pass
$cmd TypeInfo type-1 # should show object-01 .. object-04
$cmd TypeInfo type-2 # should show object-01 .. object-05
$cmd TypeInfo type-3 # should show no objects (not fail)

# add a bad type name - should fail
echo TypeInfo test - empty type - should fail
$cmd SetType object ""

read -p "check finished?" ck


# add operations:
#	op-01 for domain-01,type-01, op-02 for domain-02,type-02, etc.
#	op-01, op-02, op-03, op-04, op-05 for domain-01,{type-01 .. type-05}; etc.

echo AddAccess test - should pass
for n in `seq -f '%02.0f' 5`; do
	$cmd AddAccess op-$n domain-$n type-$n ;
	for m in `seq -f '%02.0f' 5`; do
		$cmd AddAccess op-$m domain-$n type-$m ;
	done;
done
read -p "check finished?" ck

# check access for user, object
# these should succeed
echo CanAccess test - should pass

for n in `seq -f '%02.0f' 5`; do
	for m in `seq -f '%02.0f' 5`; do
		$cmd CanAccess op-$m user-$n object-$m ;
	done;
done

# these should fail
echo CanAccess test - should fail
$cmd CanAccess op-1 user-99 object-99
$cmd CanAccess op-99 user-01 object-01

rm -rf ~/a1/test/*
cd ~/a1/test/
