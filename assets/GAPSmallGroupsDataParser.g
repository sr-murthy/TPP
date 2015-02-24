LoadPackage( "sonata" );


NumberOfSmallGroups := function( range )

  return Sum( List( range, N -> NumberSmallGroups( N ) ) );

  end;


NilpClass := function( G )

  if IsNilpotent( G ) then
    return NilpotencyClassOfGroup( G );
  else
    return "null";
  fi;

  end;


SolvableLength := function( G )

  if IsSolvable( G ) then
    return DerivedLength( G );
  else
    return "null";
  fi;

  end;


Generators := function( G )

  return List( GeneratorsOfGroup( G ), g -> [g,Order(g)] );

  end;


D3 := function( G )

  local x, DG;

  DG := 0;
  for x in CharacterDegrees( G ) do
    DG := DG + x[2]*( x[1]^3 );
  od;

  return DG;

  end;


IndexLargestAbelianNormalSubgroup := function( G )

  local li;

  li := List( Filtered( Subgroups( G ),
              H -> IsAbelian( H ) and IsNormal( G, H ) and Order( H ) > 1 ),
              K -> IndexNC( G, K ) );
  if li = [] then
    return "null";
  else
    return li[Length( li )];
  fi;

  end;


IndexLargestCyclicNormalSubgroup := function( G )

  local li;

  li := List( Filtered( Subgroups( G ),
              H -> IsCyclic( H ) and IsNormal( G, H ) and Order( H ) > 1 ),
              K -> IndexNC( G, K ) );
  if li = [] then
    return "null";
  else
    return li[Length( li )];
  fi;

  end;


IndexLargestElementaryAbelianNormalSubgroup := function( G )

  local li;

  li := List( Filtered( Subgroups( G ),
              H -> IsElementaryAbelian( H ) and IsNormal( G, H ) and Order( H ) > 1 ),
              K -> IndexNC( G, K ) );
  if li = [] then
    return "null";
  else
    return li[Length( li )];
  fi;

  end;


# GAP function for printing the JSON object information of a group in the GAP Small Groups # Library.

AsJSONObject := function( G )

  return Concatenation(
    "{\"GAP_ID\": ", String( IdSmallGroup( G ) ), ",",
     "\"GAP_desc\": \"", String( StructureDescription( G ) ), "\",",
     "\"GAP_pickled_ID\": ", "null", ",",
     "\"index_LAN_subgroup\": ", String( IndexLargestAbelianNormalSubgroup( G ) ), ",",
     "\"index_LCN_subgroup\": ", String( IndexLargestCyclicNormalSubgroup( G ) ), ",",
     "\"index_LEAN_subgroup\": ", String( IndexLargestElementaryAbelianNormalSubgroup( G ) ), ",",
     "\"is_abelian\": ", String( IsAbelian( G ) ), ",",
     "\"comm_length\": ", String( CommutatorLength( G ) ), ",",
     "\"is_cyclic\": ", String( IsCyclic( G ) ), ",",
     "\"is_elem_abelian\": ", String( IsElementaryAbelian( G ) ), ",",
     "\"is_simple\": ", String( IsSimple( G ) ), ",",
     "\"comp_length\": ", String( Size( CompositionSeries( G ) ) - 1 ), ",",
     "\"is_nilpotent\": ", String( IsNilpotent( G ) ), ",",
     "\"nilpotency_class\": ", String( NilpClass( G ) ), ",",
     "\"is_solvable\": ", String( IsSolvable( G ) ), ",",
     "\"derived_length\": ", String( SolvableLength( G ) ), ",",
     "\"is_pgroup\": ", String( IsPGroup( G ) ), ",",
     "\"generators\": \"", String( Generators( G ) ), "\",",
     "\"char_degrees\": \"", String( CharacterDegrees( G ) ), "\"}" );

  end;

WriteSmallGroupsJSONFile := function( file_dir, file_name, orders, inc_abelian )

  local file, n, i, num_small_groups, G, total_groups, total_bytes;

  LoadPackage( "IO" );
  file := IO_File( Concatenation( file_dir, file_name ), "w" );
  total_groups := 0;
  total_bytes := 0;

  IO_WriteLine( file, "[" );
  for n in orders do
    num_small_groups := NumberSmallGroups( n );
    for i in [1..num_small_groups] do
      G := SmallGroup( n, i );
      if inc_abelian then
        if total_groups > 0 then
          total_bytes := total_bytes + IO_WriteLine( file, "," );
        fi;
        total_bytes := total_bytes + IO_Write( file, AsJSONObject( G ) );
        total_groups := total_groups + 1;
      else
        if not IsAbelian( G ) then
          if total_groups > 0 then
            total_bytes := total_bytes + IO_WriteLine( file, "," );
          fi;
          total_bytes := total_bytes + IO_Write( file, AsJSONObject( G ) );
          total_groups := total_groups + 1;
        fi;
      fi;
    od;
  od;
  total_bytes := total_bytes + IO_WriteFlush( file, "\n]" );

  IO_Close( file );

  Print( total_groups, " small groups successfully written as JSON objects to file ",
         Concatenation( file_dir, file_name ), " using ", Float( total_bytes / 1024 ),
         " Kb." );

  end;
